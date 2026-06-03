import os
import random
import json
import re
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="PCB MST AI Service",
    description="Gemini API kullanarak sentetik PCB topolojisi üretir",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

PCB_COMPONENTS = (
    [f"R{i}" for i in range(1, 21)] +
    [f"C{i}" for i in range(1, 16)] +
    [f"IC{i}" for i in range(1, 11)] +
    [f"U{i}" for i in range(1, 11)] +
    [f"Q{i}" for i in range(1, 11)] +
    [f"D{i}" for i in range(1, 11)] +
    [f"L{i}" for i in range(1, 8)]  +
    [f"T{i}" for i in range(1, 6)]  +
    [f"SW{i}" for i in range(1, 6)] +
    [f"LED{i}" for i in range(1, 6)] +
    [f"JP{i}" for i in range(1, 6)] +
    ["VCC", "GND", "VDD", "VSS", "VREF", "AGND", "DGND"]
)


class TopologyRequest(BaseModel):
    node_count: Optional[int] = 8
    max_weight: Optional[int] = 100
    density: Optional[str] = "medium"  # low | medium | high


class TopologyResponse(BaseModel):
    nodes: list[str]
    edges: list[dict]
    description: str
    generated_by: str


def generate_fallback_topology(node_count: int, max_weight: int, density: str) -> dict:
    """Gemini API yoksa veya hata verirse deterministik ama random topoloji üretir."""
    nodes = random.sample(PCB_COMPONENTS, min(node_count, len(PCB_COMPONENTS)))

    density_map = {"low": 1.2, "medium": 1.8, "high": 2.5}
    edge_multiplier = density_map.get(density, 1.8)
    target_edges = int(len(nodes) * edge_multiplier)

    edges = []
    seen = set()

    # Önce spanning tree oluştur (bağlantılılığı garantile)
    shuffled = nodes[:]
    random.shuffle(shuffled)
    for i in range(1, len(shuffled)):
        u, v = shuffled[i - 1], shuffled[i]
        w = random.randint(1, max_weight)
        edges.append({"source": u, "target": v, "weight": w})
        seen.add((min(u, v), max(u, v)))

    # Ekstra kenarlar ekle
    attempts = 0
    while len(edges) < target_edges and attempts < 500:
        u, v = random.sample(nodes, 2)
        key = (min(u, v), max(u, v))
        if key not in seen:
            w = random.randint(1, max_weight)
            edges.append({"source": u, "target": v, "weight": w})
            seen.add(key)
        attempts += 1

    return {
        "nodes": nodes,
        "edges": edges,
        "description": f"Fallback: {len(nodes)} bileşen, {len(edges)} olası bağlantı, yoğunluk={density}",
        "generated_by": "fallback_random"
    }


async def generate_with_gemini(node_count: int, max_weight: int, density: str) -> dict:
    """Gemini API ile topoloji üretir."""
    prompt = f"""
Sen bir PCB (Printed Circuit Board) tasarım asistanısın.
{node_count} adet PCB bileşeni ve aralarındaki ağırlıklı bağlantıları içeren
sentetik bir PCB topolojisi üret.

Kurallar:
- Bileşen isimleri gerçekçi PCB component adları olsun (R1, C2, IC1, U1, VCC, GND vb.)
- Kenar ağırlıkları 1-{max_weight} arasında olsun (kısa=düşük, uzun=yüksek maliyet)
- Yoğunluk: {density} (low=az kenar, medium=orta, high=çok kenar)
- Graf bağlı (connected) olmalı
- Döngüler içerebilir (MST algoritması bunları kaldıracak)

SADECE aşağıdaki JSON formatında yanıt ver, başka hiçbir şey yazma:
{{
  "nodes": ["R1", "C1", "IC1", ...],
  "edges": [
    {{"source": "R1", "target": "C1", "weight": 15}},
    ...
  ],
  "description": "kısa açıklama"
}}
"""

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.7, "maxOutputTokens": 1024}
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        resp.raise_for_status()
        data = resp.json()

    raw_text = data["candidates"][0]["content"]["parts"][0]["text"]

    # JSON bloğunu temizle
    clean = re.sub(r"```(?:json)?", "", raw_text).strip().strip("`").strip()
    result = json.loads(clean)
    result["generated_by"] = "gemini"
    return result


@app.get("/health")
def health():
    has_key = bool(GEMINI_API_KEY)
    return {
        "status": "ok",
        "service": "ai-service",
        "gemini_configured": has_key
    }


@app.post("/api/topology", response_model=TopologyResponse)
async def generate_topology(req: TopologyRequest):
    """Sentetik PCB topolojisi üretir. Gemini varsa Gemini, yoksa fallback kullanır."""
    node_count = max(3, min(req.node_count or 8, 100, len(PCB_COMPONENTS)))
    max_weight = max(1, min(req.max_weight or 100, 1000))
    density = req.density or "medium"

    if GEMINI_API_KEY:
        try:
            result = await generate_with_gemini(node_count, max_weight, density)
            return TopologyResponse(**result)
        except Exception as e:
            # Gemini başarısız olursa fallback'e düş
            print(f"Gemini error, using fallback: {e}")

    result = generate_fallback_topology(node_count, max_weight, density)
    return TopologyResponse(**result)


@app.get("/api/topology/sample")
async def get_sample():
    """Hızlı test için sabit örnek topoloji döndürür."""
    return {
        "nodes": ["VCC", "GND", "R1", "R2", "C1", "IC1", "U1", "D1"],
        "edges": [
            {"source": "VCC", "target": "R1", "weight": 5},
            {"source": "VCC", "target": "IC1", "weight": 12},
            {"source": "R1", "target": "C1", "weight": 8},
            {"source": "R1", "target": "R2", "weight": 3},
            {"source": "R2", "target": "IC1", "weight": 7},
            {"source": "C1", "target": "GND", "weight": 4},
            {"source": "IC1", "target": "U1", "weight": 10},
            {"source": "IC1", "target": "D1", "weight": 6},
            {"source": "U1", "target": "GND", "weight": 9},
            {"source": "D1", "target": "GND", "weight": 2},
            {"source": "R2", "target": "U1", "weight": 15},
        ],
        "description": "Örnek PCB: güç hattı + IC + pasif elemanlar",
        "generated_by": "sample"
    }
