# Frontend (Vanilla HTML + JavaScript + Cytoscape.js)

PCB MST Optimizer'ın kullanıcı arayüzü. Herhangi bir çatı (React/Vite) kullanmadan, tek bir `index.html` içinde çalışır — bağımlılık derdi olmadan doğrudan tarayıcıda açılır.

Sunduğu özellikler:
- Grafı 2B düzlemde **Cytoscape.js** ile çizme
- "MST hesapla" ile seçilen kenarları **yeşil animasyonla** vurgulama
- Düğüm/kenar ekleme ve silme — dinamik güncelleme sonrası MST yeniden hesaplanır
- BFS/DFS bağlılık testi
- AI servisinden topoloji üretme veya hazır örnek yükleme
- Canlı log paneli ve servis sağlık rozetleri

## Yapı

```
frontend/
├── index.html          # Tüm arayüz + uygulama mantığı (JavaScript)
├── cytoscape.min.js    # Graf görselleştirme kütüphanesi
├── nginx.conf          # Statik sunum yapılandırması
└── Dockerfile          # nginx:alpine ile servis eder
```

> Not: `src/` altındaki React bileşenleri projenin erken bir denemesidir ve **kullanılmaz**; çalışan arayüz `index.html`'dir.

## Çalıştırma

```bash
# Docker (önerilen — nginx ile sunum)
docker compose up frontend          # http://localhost:3000

# Lokal: index.html'i tarayıcıda aç, ya da basit bir statik sunucuyla:
python -m http.server 3000
```

Arayüz, backend'i `http://localhost:8000` ve AI servisini `http://localhost:8001` üzerinden çağırır; bu iki servisin de ayakta olması gerekir.

## Sorumlu

Üye 3 — `feature/uye3-frontend-ai`
