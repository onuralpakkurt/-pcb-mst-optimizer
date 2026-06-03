# AI Service

PCB MST Optimizer'ın yapay zeka servisi. Tek görevi vardır: backend'i ve görselleştirmeyi denemek için **sentetik PCB topolojileri üretmek**. MST hesaplama, optimizasyon ya da graf analizi yapmaz — bunların tamamı backend'in kendi yazdığımız algoritmalarındadır. (Ödevde GenAI yalnızca opsiyonel bir yardımcı araçtır.)

Topolojiyi **Google Gemini** (`gemini-2.5-flash`) üretir. Anahtar tanımlı değilse ya da çağrı başarısız olursa servis, deterministik bir rastgele üreticiye (fallback) düşer: önce bir spanning tree kurarak grafın **bağlı** olmasını garanti eder, sonra istenen yoğunluğa göre ekstra kenar ekler. Böylece anahtar olsun olmasın her zaman geçerli, bağlı bir graf döner.

## Yapı

Servis tek bir dosyadan oluşur:

```
ai-service/
├── main.py             # FastAPI uygulaması (Gemini çağrısı + fallback)
├── requirements.txt
└── Dockerfile
```

## Endpoint'ler

| Method | Endpoint | Amaç |
|---|---|---|
| GET  | `/health` | Sağlık durumu + Gemini anahtarı tanımlı mı |
| POST | `/api/topology` | Sentetik topoloji üret (`node_count`, `density`, `max_weight`) |
| GET  | `/api/topology/sample` | Hızlı test için sabit örnek topoloji |

## Gemini Anahtarı (opsiyonel)

Proje kökündeki `.env` dosyasından okunur (commit edilmez — `.gitignore`'da). Verilmezse fallback devreye girer:

```
GEMINI_API_KEY=...
```

## Çalıştırma

```bash
# Lokal
uvicorn main:app --reload --port 8001

# Docker
docker compose up ai-service
```

## Sorumlu

Üye 3 — `feature/uye3-frontend-ai`
