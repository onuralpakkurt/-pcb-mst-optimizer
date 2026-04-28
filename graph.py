class Graph:

    def __init__(self):
        self._adjacency = {}
        self._vertex_count = 0
        self._edge_count = 0

    def add_vertex(self, node):
        if node not in self._adjacency:
            self._adjacency[node] = {}
            self._vertex_count += 1

    def add_edge(self, node1, node2, weight):
        if node1 not in self._adjacency:
            self.add_vertex(node1)
        if node2 not in self._adjacency:
            self.add_vertex(node2)

        is_new = node2 not in self._adjacency[node1]

        self._adjacency[node1][node2] = weight
        self._adjacency[node2][node1] = weight

        if is_new:
            self._edge_count += 1

    def get_neighbors(self, node):
        if node not in self._adjacency:
            raise KeyError(f"Vertex '{node}' not found in graph")
        return dict(self._adjacency[node])

    def get_all_vertices(self):
        return list(self._adjacency.keys())

    def get_all_edges(self):
        edges = []
        seen = set()
        for u in self._adjacency:
            for v, weight in self._adjacency[u].items():
                edge_id = frozenset({u, v})
                if edge_id not in seen:
                    seen.add(edge_id)
                    edges.append((u, v, weight))
        return edges

    def remove_vertex(self, node):
        if node not in self._adjacency:
            raise KeyError(f"Vertex '{node}' not found in graph")

        for neighbor in list(self._adjacency[node].keys()):
            del self._adjacency[neighbor][node]
            self._edge_count -= 1

        del self._adjacency[node]
        self._vertex_count -= 1

    def remove_edge(self, node1, node2):
        if node1 not in self._adjacency:
            raise KeyError(f"Vertex '{node1}' not found in graph")
        if node2 not in self._adjacency:
            raise KeyError(f"Vertex '{node2}' not found in graph")
        if node2 not in self._adjacency[node1]:
            raise KeyError(f"Edge between '{node1}' and '{node2}' not found")

        del self._adjacency[node1][node2]
        del self._adjacency[node2][node1]
        self._edge_count -= 1

    def vertex_count(self):
        return self._vertex_count

    def edge_count(self):
        return self._edge_count

    def __str__(self):
        lines = [f"Graph with {self._vertex_count} vertices and {self._edge_count} edges"]
        seen = set()
        for u in self._adjacency:
            for v, w in self._adjacency[u].items():
                edge_id = frozenset({u, v})
                if edge_id not in seen:
                    seen.add(edge_id)
                    lines.append(f"  {u} -- {w} -- {v}")
        return "\n".join(lines)

    def __repr__(self):
        return f"Graph(vertices={self._vertex_count}, edges={self._edge_count})"
