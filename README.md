# -pcb-mst-optimizer

# PCB MST Optimizer

  Karmaşık bir elektronik anakart (PCB) üzerindeki bileşenlerin (dirençler, kapasitörler, güç kaynakları) birbirine bağlanmasını
  **Minimum Spanning Tree (MST)** algoritması ile optimize eden web tabanlı simülasyon sistemi.

  > Veri Yapıları dersi grup projesi — Bahar 2026

  ---

  ## Ekip

  | İsim | GitHub | Sorumluluk |
  |---|---|---|
  | Onuralp Akkurt | [@onuralpakkurt](https://github.com/onuralpakkurt) | Backend / Veri Yapıları |
  | Uye Iki | @kullaniciadi | Algoritma / API |
  | Uye Uc | @kullaniciadi | Frontend / AI Servisi |

  > Not: Kod ve veritabanı içinde isimler **Türkçe karaktersiz** yazılmıştır.

  ---

  ## Hedef

  PCB bileşenlerini düğüm, aralarındaki olası bağlantıları ağırlıklı kenar olarak modelleyip, **toplam bağlantı maliyeti minimum** ve
  **döngü içermeyen** bir bağlantı ağı (MST) hesaplayan, görselleştiren ve dinamik düğüm eklemeye izin veren tam fonksiyonel bir
  sistemdir.

  ---

  ## Mimari

  3 bağımsız servis, hepsi `docker-compose up` ile tek komutta ayağa kalkar:

  - **Backend** (Python/FastAPI): Sıfırdan yazılmış veri yapıları (Graph, UnionFind, Queue, Stack) + Kruskal MST algoritması + REST API
  - **Frontend** (React + Cytoscape.js): Graf görselleştirme, MST animasyonu, dinamik düğüm ekleme arayüzü
  - **AI Service** (Python + Gemini API): Sentetik PCB topolojisi üretimi + MST iyileştirme yorumu

  ---

  ## Teknolojiler

  - **Backend**: Python 3.11, FastAPI, Pydantic, Uvicorn
  - **Frontend**: React 18, Vite, Cytoscape.js, Axios
  - **AI**: Python, Google Generative AI (Gemini)
  - **Container**: Docker, docker-compose
  - **Versiyon kontrolü**: Git, GitHub (feature branch + PR akışı)

  ---

  ## Algoritma

  - **MST**: Kruskal Algoritması — `O(E log E)`
  - **Yardımcı veri yapısı**: Union-Find (path compression + union by rank) — `O(α(N))` amortize
  - **Bağlantılılık kontrolü**: BFS ve DFS — `O(V + E)`

  ---

  ## Branch Stratejisi

  - `main` — korumalı, direkt push yok, sadece PR ile merge
  - `feature/uye1-backend-data-structures` — Veri yapıları
  - `feature/uye2-algorithms-api` — Algoritmalar + API
  - `feature/uye3-frontend-ai` — Frontend + AI servisi

  Her ekip üyesi kendi feature branch'inde çalışır, modülü tamamlandıkça `main`'e Pull Request açar.

  ---

  ## Güncel Durum

  ### Tamamlanan
  - [x] GitHub reposu kuruldu
  - [x] Branch koruma kuralları aktif
  - [x] 3 feature branch oluşturuldu
  - [x] Mimari ve teknoloji seçimleri yapıldı

  ### Devam Eden
  - [ ] Klasör iskeletinin oluşturulması
  - [ ] Backend veri yapılarının yazımı
  - [ ] Algoritma + API geliştirme
  - [ ] Frontend görselleştirme
  - [ ] AI servisi entegrasyonu
  - [ ] Docker konfigürasyonu
  - [ ] UML ve Big-O dokümantasyonu
  - [ ] Demo videosu

  ---

  ## Kurulum

  > Yapım aşamasında. Tamamlandığında:

  ```bash
  git clone https://github.com/onuralpakkurt/-pcb-mst-optimizer.git
  cd -pcb-mst-optimizer
  docker-compose up --build

  Frontend: http://localhost:3000
  Backend API: http://localhost:8000/docs
