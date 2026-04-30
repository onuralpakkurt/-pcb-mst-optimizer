
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

  ---

  ## Hedef

  PCB bileşenlerini düğüm, aralarındaki olası bağlantıları ağırlıklı kenar olarak modelleyip, toplam bağlantı maliyeti minimum ve döngü
  içermeyen bir bağlantı ağı (MST) hesaplayan, görselleştiren ve dinamik düğüm eklemeye izin veren tam fonksiyonel bir sistemdir.

  ---

  ## Mimari

  3 bağımsız servis, hepsi `docker-compose up` ile tek komutta ayağa kalkar:

  - **Backend** (Python/FastAPI): Sıfırdan yazılmış veri yapıları + Kruskal MST + REST API
  - **Frontend** (React + Cytoscape.js): Graf görselleştirme, MST animasyonu, dinamik düğüm ekleme
  - **AI Service** (Python + Gemini API): Sentetik PCB topolojisi üretimi + MST iyileştirme yorumu

  ---

  ## Teknolojiler

  Python 3.11, FastAPI, React 18, Vite, Cytoscape.js, Docker, GitHub

  ---

  ## Algoritma

  - **MST**: Kruskal — `O(E log E)`
  - **Yardımcı**: Union-Find (path compression + union by rank) — `O(α(N))`
  - **Bağlantılılık**: BFS / DFS — `O(V + E)`

  ---

  ## Branch Stratejisi

  - `main` — korumalı, sadece PR ile merge
  - `feature/uye1-backend-data-structures`
  - `feature/uye2-algorithms-api`
  - `feature/uye3-frontend-ai`

  ---

  ## Güncel Durum

  - [x] GitHub reposu kuruldu
  - [x] Branch koruması aktif
  - [x] 3 feature branch oluşturuldu
  - [x] Klasör iskeleti oluşturuldu
  - [ ] Backend veri yapıları
  - [ ] Algoritma + API
  - [ ] Frontend
  - [ ] AI servisi
  - [ ] Docker
  - [ ] Demo videosu

  ---

  ## Kurulum

  ```bash
  git clone https://github.com/onuralpakkurt/-pcb-mst-optimizer.git
  cd -pcb-mst-optimizer
  docker-compose up --build
  ```

