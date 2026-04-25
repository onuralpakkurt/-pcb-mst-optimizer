# Frontend (React + Cytoscape.js)

PCB MST Optimizer'ın kullanıcı arayüzü. Graf görselleştirme, MST animasyonu ve dinamik düğüm ekleme özellikleri sunar.

## Klasör Yapısı

```
frontend/
└── src/
    ├── App.jsx
    ├── components/
    │   ├── GraphCanvas.jsx   # Cytoscape.js graf canvas
    │   ├── MstAnimator.jsx   # MST kenar animasyonu
    │   ├── NodeAdder.jsx     # Dinamik düğüm ekleme UI
    │   └── AiPanel.jsx       # AI senaryo + öneri paneli
    └── api/
        └── client.js         # Backend HTTP client (axios)
```

## Çalıştırma

```bash
# Lokal
npm install
npm run dev

# Docker
docker-compose up frontend
```

Frontend: `http://localhost:3000`

## Sorumlu

Üye 3 — `feature/uye3-frontend-ai`
