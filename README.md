# PCB MST Optimizer

Karmaşık bir elektronik anakart (PCB) üzerindeki bileşenleri — dirençler, kapasitörler, entegreler, güç hatları — birbirine **en az toplam maliyetle, döngü oluşturmadan ve hiçbirini dışarıda bırakmadan** bağlayan en uygun bağlantı ağını bulan web tabanlı bir simülasyon sistemi.

Bileşenler birer **düğüm**, aralarında çekilebilecek olası bağlantılar **ağırlıklı kenar** olarak modellenir. **Kruskal algoritması** bu kenarlar arasından, tüm bileşenleri en ucuz şekilde birbirine bağlayan ağacı (**Minimum Spanning Tree**) seçer. Kullanıcı arayüzden yeni düğüm/kenar ekledikçe ağ anında yeniden hesaplanıp görselleştirilir.

> Veri Yapıları dersi grup projesi — Bahar 2026

---

## 📄 Detaylı Proje Raporu

> ## 👉 **[Tam Proje Raporu → `docs/PROJE_RAPORU.md`](docs/PROJE_RAPORU.md)**
>
> **UML diyagramları · Big-O (zaman/uzay) analizi · AI prompt dökümü · test sonuçları** — hepsi tek dosyada. GitHub'da diyagramlar otomatik render olur.

---

## Ekip

| Üye | İsim | GitHub | Sorumluluk | Branch |
|---|---|---|---|---|
| 1 | Mehmet Kusgul | — | Backend / Veri Yapıları | `feature/uye1-backend-data-structures` |
| 2 | Sinasi Onuralp Akkurt | [@onuralpakkurt](https://github.com/onuralpakkurt) | Algoritma / API | `feature/uye2-algorithms-api` |
| 3 | Zafer Tuna | — | Frontend / AI Servisi | `feature/uye3-frontend-ai` |

---

## Nasıl Çalışır?

Sistem, birbirinden bağımsız çalışan **üç mikroservisten** oluşur ve tek bir `docker compose up` komutuyla ayağa kalkar:

- **Frontend** (Vanilla HTML + JavaScript + Cytoscape.js) — Grafı tarayıcıda çizer. "MST hesapla" dendiğinde seçilen kenarlar **yeşil animasyonla** belirir; kullanıcı düğüm veya kenar ekledikçe ağ güncellenir ve MST yeniden hesaplanır.
- **Backend** (Python / FastAPI) — Projenin kalbi. Graf, Union-Find, Queue ve Stack **sıfırdan** yazılmıştır; Kruskal MST hesabı ile BFS/DFS bağlılık testleri burada koşar ve REST API üzerinden sunulur.
- **AI Service** (Python / Google Gemini) — Test için sentetik PCB topolojileri üretir. Gemini anahtarı yoksa deterministik rastgele üretime (fallback) düşerek **her durumda** geçerli bir graf döndürür. Optimizasyon kararı vermez; o iş tamamen backend'in kendi algoritmalarındadır.

```
[Frontend]  ←→  [Backend API]  ←→  [AI Service]
 :3000           :8000              :8001
```

---

## Sıfırdan Yazılan Veri Yapıları

Şartname gereği hazır veri yapısı kütüphaneleri (`heapq`, `collections.deque`, `networkx` vb.) kullanılmadan, tümü `backend/app/data_structures/` altında elle yazıldı:

- **Graph** — Komşuluk listesi (dict-of-dict), yönsüz ve ağırlıklı; devre topolojisini modeller.
- **Union-Find** — Path compression + union by rank; Kruskal'da döngüleri engeller, neredeyse sabit zamanda çalışır.
- **Queue** — Tekli bağlı liste (head + tail işaretçili); BFS için gerçek O(1) ekleme/çıkarma sağlar.
- **Stack** — LIFO; DFS dolaşımında kullanılır.

---

## Algoritmalar ve Karmaşıklık

Tüm bileşenleri minimum maliyetle bağlayan ağ **Kruskal** ile bulunur; grafın bağlı olup olmadığı **BFS/DFS** ile doğrulanır.

| Algoritma / Yapı | Karmaşıklık | Kullanım |
|---|---|---|
| Kruskal (MST) | O(E log E) | MST hesaplama |
| Union-Find (PC + UbR) | ~O(1) amortize | Döngü kontrolü |
| BFS / DFS | O(V + E) | Bağlılık testi |

Ayrıntılı türetme ve gerçek ölçümler (100 düğüm / 250 kenar → ~5 ms) [proje raporunda](docs/PROJE_RAPORU.md).

---

## Çalıştırma

### Docker (önerilen — tek komut)

```bash
# (opsiyonel) AI için Gemini anahtarı — verilmezse fallback çalışır
echo "GEMINI_API_KEY=..." > .env

docker compose up --build
```

- Arayüz → http://localhost:3000
- API (Swagger UI) → http://localhost:8000/docs

### Yerel (sadece backend)

```bash
cd backend
python -m venv venv
source venv/Scripts/activate        # Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Sistem; bilinen graflarda MST sonuçları elle doğrulanarak, sınır durumlar (kopuk graf, self-loop, boş graf) ve üç servisin Docker'la birlikte çalışması üzerinden uçtan uca test edilmiştir (ayrıntılar raporun test bölümünde).

---

## API Özeti

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

## Sürüm Kontrolü

`main` korumalı daldır — doğrudan push yapılmaz. Geliştirme her üyenin kendi feature branch'inde yürütülür, kod incelemesinden sonra Pull Request ile `main`'e merge edilir.

---

## Lisans

MIT
