# PCB MST Optimizer - Frontend

Bu klasör, PCB MST Optimizer projesinin kullanıcı arayüzü bölümünü içerir. Frontend tarafı React ile geliştirilecek ve PCB üzerindeki bileşenlerin graf yapısı şeklinde görselleştirilmesini sağlayacaktır.

## Amaç

Frontend’in temel amacı, backend tarafından sağlanan PCB bileşenlerini ve bağlantılarını kullanıcıya görsel olarak sunmaktır. PCB bileşenleri düğüm, bileşenler arasındaki bağlantılar ise ağırlıklı kenar olarak gösterilecektir.

Minimum Spanning Tree sonucu hesaplandıktan sonra, seçilen MST kenarları arayüz üzerinde vurgulanacaktır.

## Planlanan Özellikler

- PCB bileşenlerini graf olarak görselleştirme
- Direnç, kapasitör ve güç kaynağı gibi bileşenleri düğüm olarak gösterme
- Bileşenler arasındaki bağlantıları ağırlıklı kenar olarak gösterme
- MST sonucunu farklı biçimde vurgulama
- Dinamik düğüm ekleme arayüzü hazırlama
- Backend API ile veri alışverişi yapma
- AI servisinden gelen senaryo ve yorumları kullanıcıya gösterme

## Klasör Yapısı
frontend/
└── src/
    ├── App.jsx
    ├── components/
    │   ├── GraphCanvas.jsx
    │   ├── MstAnimator.jsx
    │   ├── NodeAdder.jsx
    │   └── AiPanel.jsx
    └── api/
        └── client.js
