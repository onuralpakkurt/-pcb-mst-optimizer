# AI Service

PCB MST Optimizer'ın yapay zeka servisi. Gemini (veya OpenAI) API'sini kullanarak iki görev üstlenir:

1. **Sentetik PCB topolojisi üretimi** — verilen düğüm sayısı ve senaryo için JSON formatında graf üretir
2. **MST iyileştirme yorumu** — hesaplanan MST'yi inceleyip doğal dil ile öneri sunar

## Klasör Yapısı

```
ai-service/
└── app/
    ├── main.py              # FastAPI uygulama girişi
    ├── routes.py            # /generate-topology, /analyze-mst
    └── prompts/             # AI prompt template'leri
        ├── topology_gen.txt
        └── mst_analysis.txt
```

## Çevre Değişkenleri

`.env` dosyası gerekli (commit edilmez):

```
GEMINI_API_KEY=...
```

## Çalıştırma

```bash
# Lokal
uvicorn app.main:app --reload --port 8001

# Docker
docker-compose up ai-service
```

## Sorumlu

Üye 3 — `feature/uye3-frontend-ai`
