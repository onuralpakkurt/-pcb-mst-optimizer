from app.data_structures import Graph, UnionFind


def kruskal(graph: Graph) -> dict:
    vertices = graph.get_all_vertices()
    edges = graph.get_all_edges()

    edges_sorted = sorted(edges, key=lambda edge: edge[2])

    uf = UnionFind()
    for vertex in vertices:
        uf.make_set(vertex)

    mst_edges = []
    total_cost = 0.0
    target_edge_count = max(0, len(vertices) - 1)

    for u, v, weight in edges_sorted:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, weight))
            total_cost += weight
            if len(mst_edges) == target_edge_count:
                break

    is_complete = len(mst_edges) == target_edge_count and len(vertices) > 0

    return {
        "edges": mst_edges,
        "total_cost": total_cost,
        "edge_count": len(mst_edges),
        "is_complete": is_complete,
    }
