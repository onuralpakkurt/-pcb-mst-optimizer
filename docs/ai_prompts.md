# AI Prompt Dökümleri

> Bu doküman AI servisine gönderilen tüm prompt'ları tarih + amaç + cevap ile birlikte tutar. Şartname gereği teslim edilecek.

---

## AI Servisinin Kapsamı

Bu projede AI **sadece** sentetik (test amaçlı) PCB graf topolojisi üretmek için kullanılmaktadır. MST hesaplama, optimizasyon kararı veya graf analizi gibi işler **AI tarafından yapılmamaktadır** — bunların hepsi backend'deki kendi yazdığımız algoritmalar tarafından yürütülmektedir.

**Model:** Google Gemini API (gemini-2.0-flash veya benzeri)

**Endpoint:** `POST /generate-topology` (AI Service)

---

## Format

Her prompt çağrısı için aşağıdaki şablon doldurulur:

```
### YYYY-MM-DD HH:MM — [Görev]

**Amaç:** [Ne için kullanıldı]
**Model:** gemini-2.0-flash
**Token kullanımı:** [prompt_tokens + response_tokens]

**Prompt:**
\`\`\`
[Tam prompt metni]
\`\`\`

**Cevap (JSON):**
\`\`\`json
[Modelin döndürdüğü JSON]
\`\`\`

**Sonuç:** [Üretilen graf bilgisi — vertex/edge sayısı, başarılı mı]
```

---

## Örnek Prompt Şablonu (Üye 3 tarafından implement edilecek)

```
You are generating synthetic test data for a PCB (printed circuit board) component graph.
Generate exactly N components and a set of weighted edges between them.

Requirements:
- N components, types from: ["resistor", "capacitor", "inductor", "ic", "led", "diode"]
- Each component has a unique ASCII id (e.g. "R1", "C1", "U1", "L1")
- Edges are undirected, weighted (weight = approximate trace length in mm, range 1-50)
- Average degree per node should be 2-4 (sparse graph, like real PCBs)
- The graph should be connected (every component reachable)

Return ONLY valid JSON, no markdown fences, no commentary:
{
  "vertices": [{"id": "R1", "type": "resistor"}, ...],
  "edges": [{"from": "R1", "to": "C1", "weight": 12.5}, ...]
}
```

Parametre `N` runtime'da değişecek (örn. 20, 50, 100 düğüm).

---

## Loglar

> Bu bölüm her AI çağrısı sonrasında AI servisi tarafından otomatik doldurulacak. Şu an boş.

_Henüz prompt log'u bulunmamaktadır._
