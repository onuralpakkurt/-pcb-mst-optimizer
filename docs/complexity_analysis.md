# Karmaşıklık Analizi (Big-O)

> Bu doküman implementasyon ilerledikçe doldurulacaktır.

## Veri Yapıları

### Graph (Adjacency List)
| Operasyon | Zaman | Uzay |
|---|---|---|
| `add_node` | O(1) | O(V) |
| `add_edge` | O(1) | O(E) |
| `get_neighbors(v)` | O(deg(v)) | — |
| `is_connected` (BFS) | O(V + E) | O(V) |

### Union-Find (path compression + union by rank)
| Operasyon | Zaman amortize | Uzay |
|---|---|---|
| `find(x)` | O(α(N)) ≈ O(1) | O(N) |
| `union(x, y)` | O(α(N)) ≈ O(1) | — |

### Queue / Stack
| Operasyon | Zaman | Uzay |
|---|---|---|
| `enqueue` / `push` | O(1) amortize | O(N) |
| `dequeue` / `pop` | O(1) amortize | — |

## Algoritmalar

### Kruskal MST
- Toplam: **O(E log E)** = O(E log V)
- Kenar sıralama: O(E log E)
- Union-Find ile döngü kontrolü: O(E · α(N))

### BFS / DFS
- Zaman: O(V + E)
- Uzay: O(V) (Queue/Stack + visited set)

## Kaynak

- CLRS — Introduction to Algorithms, 3rd Ed.
- (Eklenmeli: kullanılan diğer kaynaklar)
