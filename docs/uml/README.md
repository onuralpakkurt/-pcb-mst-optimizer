# UML Diyagramları (Mermaid)

Bu sayfada projenin sınıf yapısı (Class Diagram), MST hesaplama iş akışı (Sequence Diagram) ve sistem mimarisi (Deployment Diagram) yer almaktadır. Markdown okuyucunuz veya GitHub Mermaid desteği sayesinde bu diyagramları doğrudan görüntüleyebilirsiniz.

---

## 1. Sınıf Diyagramı (Class Diagram)

Aşağıdaki diyagram sıfırdan yazılan veri yapılarını, API servis katmanını ve aralarındaki ilişkileri göstermektedir:

```mermaid
classDiagram
    direction TB

    class Graph {
        -dict _adjacency
        -int _vertex_count
        -int _edge_count
        +add_vertex(node)
        +add_edge(node1, node2, weight)
        +get_neighbors(node) dict
        +get_all_vertices() list
        +get_all_edges() list
        +remove_vertex(node)
        +remove_edge(node1, node2)
        +vertex_count() int
        +edge_count() int
    }

    class UnionFind {
        -dict _parent
        -dict _rank
        +make_set(node)
        +find(node)
        +union(node1, node2)
        +connected(node1, node2) bool
    }

    class Queue {
        -_Node _head
        -_Node _tail
        -int _size
        +enqueue(item)
        +dequeue() item
        +peek() item
        +is_empty() bool
        +size() int
    }

    class _Node {
        +value
        +_Node next
    }

    class Stack {
        -list _items
        +push(item)
        +pop() item
        +peek() item
        +is_empty() bool
        +size() int
    }

    class GraphService {
        -Graph _graph
        -Lock _lock
        +reset() Graph
        +add_node(node_id) int
        +add_edge(from_node, to_node, weight) int
        +get_graph() Graph
    }

    Queue "1" *-- "0..*" _Node : İçerir
    GraphService "1" *-- "1" Graph : Yönetir
    
    note for Graph "Komşuluk listesi (dict-of-dict)\nyaklaşımı ile yazılmıştır"
    note for UnionFind "Path compression ve Union by rank\noptimizasyonlarına sahiptir"
```

---

## 2. MST Hesaplama Akışı (Sequence Diagram)

Kullanıcı arayüzden MST hesaplamasını tetiklediğinde gerçekleşen akış:

```mermaid
sequenceDiagram
    autonumber
    actor User as Kullanıcı / Arayüz
    participant FE as Frontend (Cytoscape.js)
    participant BE as Backend API (FastAPI)
    participant GS as GraphService (Thread-safe)
    participant ALG as Kruskal Algoritması
    participant UF as UnionFind

    User->>FE: "MST Hesapla" Butonuna Basar
    FE->>BE: GET /api/mst
    activate BE
    BE->>GS: get_graph()
    GS-->>BE: Graph Nesnesi
    BE->>ALG: kruskal(graph)
    activate ALG
    ALG->>UF: UnionFind Örneği Oluşturur (make_set)
    loop Her Kenar İçin (Sıralı)
        ALG->>UF: find(u) ve find(v)
        alt Döngü Oluşmuyor (Temsilciler Farklı)
            ALG->>UF: union(u, v)
            ALG->>ALG: Kenarı MST listesine ekle
        end
    end
    ALG-->>BE: MST Kenarları & Toplam Maliyet & Durum
    deactivate ALG
    BE-->>FE: MSTResponse (JSON)
    deactivate BE
    FE->>User: MST Kenarlarını Yeşil Boyar & Maliyeti Gösterir
```

---

## 3. Dağıtım / Konteyner Mimarisi (Deployment Diagram)

`docker-compose` ile ayağa kalkan mikroservis mimarisi:

```mermaid
graph TD
    subgraph Docker Compose Ağı (Default Bridge)
        FE[Frontend Container<br/>Port 80/8080] <-->|HTTP API İstekleri| BE[Backend Container<br/>FastAPI / Port 8000]
        BE <-->|HTTP/REST| AI[AI Service Container<br/>Python + Gemini API / Port 8001]
    end
    
    Kullanıcı -->|Tarayıcı ile Erişim| FE
```
