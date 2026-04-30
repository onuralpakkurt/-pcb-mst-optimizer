
# PCB MST Optimizer

Karmaşık bir elektronik anakart (PCB) üzerindeki bileşenlerin (dirençler, kapasitörler, IC'ler vb.) birbirine bağlanmasını **Minimum Spanning Tree (MST)** algoritması ile optimize eden web tabanlı simülasyon sistemi.

> Veri Yapıları dersi grup projesi — Bahar 2026

---

## Ekip

| Üye | İsim | GitHub | Sorumluluk | Branch |
|---|---|---|---|---|
| 1 | Mehmet Kusgul | — | Backend / Veri Yapıları | `feature/uye1-backend-data-structures` |
| 2 | Sinasi Onuralp Akkurt | [@onuralpakkurt](https://github.com/onuralpakkurt) | Algoritma / API | `feature/uye2-algorithms-api` |
| 3 | Zafer Tuna | — | Frontend / AI Servisi | `feature/uye3-frontend-ai` |

---

## Hedef

PCB bileşenlerini düğüm, aralarındaki olası bağlantıları ağırlıklı kenar olarak modelleyip:

- Toplam bağlantı maliyeti **minimum**,
- Tüm bileşenleri **bağlayan**,
- **Döngü içermeyen**

bir bağlantı ağı (MST) hesaplayan, görselleştiren ve dinamik düğüm eklemeye izin veren tam fonksiyonel bir sistem.

---

## Mimari

3 bağımsız mikroservis, hepsi `docker-compose up` ile tek komutta ayağa kalkar:

```
[Frontend]  ←→  [Backend API]  ←→  [AI Service]
HTML + JS       Python/FastAPI      Python/Gemini
Cytoscape.js    Kruskal + UF        sentetik graf
```

- **Backend** (Python 3.11 / FastAPI): Sıfırdan yazılmış veri yapıları + Kruskal MST algoritması + REST API
- **Frontend** (Vanilla HTML + JavaScript + Cytoscape.js): Graf görselleştirme, MST animasyonu, dinamik düğüm/kenar ekleme
- **AI Service** (Python / Gemini API): Test için sentetik PCB topolojisi üretir (random graf)

---

## Teknolojiler

- **Backend:** Python 3.11, FastAPI, Uvicorn, Pydantic
- **Frontend:** HTML5, Vanilla JavaScript (ES6+), Cytoscape.js
- **AI:** Python 3.11, FastAPI, Google Gemini API
- **DevOps:** Docker, Docker Compose, GitHub (PR + branch protection)

---

## Algoritma ve Karmaşıklık

| Algoritma / Yapı | Karmaşıklık | Kullanım |
|---|---|---|
| Kruskal (MST) | O(E log E) | MST hesaplama |
| Union-Find (PC + UbR) | O(α(N)) ≈ O(1) amortize | Kruskal'da döngü kontrolü |
| BFS / DFS | O(V + E) | Graf bağlantılılık testi |
| Graph (komşuluk listesi) | add: O(1), traverse: O(V+E) | Graf modeli |

Detaylı analiz: [`docs/complexity_analysis.md`](docs/complexity_analysis.md)

---

## Veri Yapıları (Sıfırdan)

Şartname gereği hazır kütüphane (heapq, collections.deque, networkx vb.) kullanılmadı. Tüm veri yapıları sınıf bazlı, sıfırdan yazıldı:

- **`Graph`** — Komşuluk listesi (dict-of-dict), undirected, ağırlıklı
- **`UnionFind`** — Path compression + union by rank
- **`Queue`** — Singly linked list, head + tail pointer (BFS için)
- **`Stack`** — LIFO yapı (DFS için)

Konum: `backend/app/data_structures/`

---

## Branch Stratejisi

- `main` — korumalı dal, sadece **PR ile merge**, doğrudan push yasak
- `feature/uye1-backend-data-structures` — Üye 1
- `feature/uye2-algorithms-api` — Üye 2
- `feature/uye3-frontend-ai` — Üye 3

Her özellik kendi branch'inde geliştirilir, code review (≥1 onay) sonrası `main`'e merge edilir.

---

## Güncel Durum

### Tamamlanan
- [x] GitHub reposu kuruldu
- [x] Branch koruma kuralı aktif
- [x] 3 feature branch oluşturuldu
- [x] Klasör iskeleti
- [x] Veri yapıları (Graph, UnionFind, Queue, Stack) — Üye 1
- [x] Backend dosya yapısı (`backend/app/`)
- [x] FastAPI iskelet + temel endpoint'ler — Üye 2
- [x] Kruskal MST algoritması — Üye 2
- [x] BFS / DFS algoritmaları — Üye 2
- [x] Backend Dockerfile — Üye 2
- [x] Karmaşıklık analizi taslağı

### Devam Eden / Yapılacak
- [ ] Birim testler (Üye 1)
- [ ] AI servisi (Üye 3)
- [ ] Frontend (Üye 3)
- [ ] AI servisi Dockerfile (Üye 3)
- [ ] Frontend Dockerfile (Üye 3)
- [ ] docker-compose ile entegre çalıştırma (3 servis hazır olunca)
- [ ] UML diyagramları
- [ ] AI prompt logları (`docs/ai_prompts.md`)
- [ ] Demo videosu (≤10 dk)

---

## API Önizleme

Backend ayaktayken Swagger UI: `http://localhost:8000/docs`

| Method | Endpoint | Amaç |
|---|---|---|
| GET | `/health` | Servis sağlık kontrolü |
| POST | `/api/graph` | Yeni graf oluştur (sıfırla) |
| POST | `/api/graph/node` | Düğüm ekle |
| POST | `/api/graph/edge` | Ağırlıklı kenar ekle |
| GET | `/api/graph` | Mevcut grafı dön |
| GET | `/api/mst` | Kruskal ile MST hesapla |
| GET | `/api/graph/connected?algorithm=bfs\|dfs` | Graf bağlı mı? |

---

## Kurulum (Lokal Geliştirme)

```bash
# Repo klonla
git clone https://github.com/onuralpakkurt/-pcb-mst-optimizer.git
cd -pcb-mst-optimizer/backend

# Sanal ortam (Windows / bash)
python -m venv venv
source venv/Scripts/activate    # Linux/Mac: source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Backend'i çalıştır
uvicorn app.main:app --reload

# Tarayıcıda aç:
# http://localhost:8000/docs   ← Swagger UI
# http://localhost:8000/health ← health check
```

## Kurulum (Docker — yapım aşamasında)

```bash
docker-compose up --build
```

---

## Lisans

MIT
