# Backend (FastAPI)

PCB MST Optimizer'ın backend servisi. Veri yapıları sıfırdan yazılmıştır, REST API üzerinden frontend ve AI servisi ile iletişim kurar.

## Klasör Yapısı

```
backend/
├── app/
│   ├── main.py              # FastAPI uygulama girişi
│   ├── api/                 # REST endpointleri
│   ├── data_structures/     # Sıfırdan yazılmış veri yapıları
│   │   ├── graph.py         # Graph (komşuluk listesi)
│   │   ├── union_find.py    # Disjoint Set / Union-Find
│   │   ├── linked_queue.py  # FIFO Queue (BFS için, linked list)
│   │   └── stack.py         # LIFO Stack (DFS için)
│   ├── algorithms/          # MST + dolaşım algoritmaları
│   │   ├── kruskal.py
│   │   ├── bfs.py
│   │   └── dfs.py
│   └── services/            # State yönetimi (thread-safe)
└── tests/                   # Birim testler
```

## Çalıştırma

```bash
# Lokal
uvicorn app.main:app --reload --port 8000

# Docker
docker-compose up backend
```

API dokümantasyonu: `http://localhost:8000/docs`

## Sorumlular

- **Üye 1** (`feature/uye1-backend-data-structures`) — `data_structures/`
- **Üye 2** (`feature/uye2-algorithms-api`) — `algorithms/`, `api/`, `services/`, `models/`, Dockerfile
