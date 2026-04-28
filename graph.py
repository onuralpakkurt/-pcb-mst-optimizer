"""
Undirected Weighted Graph (Adjacency List)

Implementation using a plain Python dictionary. Each vertex maps to a dictionary
of neighbor -> weight.

Time Complexities:
    add_vertex(node):      O(1) — dict insertion
    add_edge(n1, n2, w):   O(1) — two dict insertions
    get_neighbors(node):   O(1) — dict lookup (returns a copy of the dict)
    get_all_vertices():    O(V) — returns list of keys
    get_all_edges():       O(E) — iterates adjacency list (visits each edge once)
    remove_vertex(node):   O(V + E_v) — removes node and all its incident edges
    remove_edge(n1, n2):   O(1) — two dict deletions
    vertex_count():        O(1) — stored counter
    edge_count():          O(1) — stored counter
"""


class Graph:
    """An undirected, weighted graph stored as an adjacency list."""

    def __init__(self):
        """Initialize an empty graph."""
        self._adjacency = {}  # dict: node -> {neighbor: weight}
        self._vertex_count = 0
        self._edge_count = 0

    def add_vertex(self, node):
        """Add a vertex to the graph.

        If the vertex already exists, this is a no-op.

        Time: O(1)
        """
        if node not in self._adjacency:
            self._adjacency[node] = {}
            self._vertex_count += 1

    def add_edge(self, node1, node2, weight):
        """Add an undirected weighted edge between node1 and node2.

        If either vertex does not exist, it is created automatically.
        If the edge already exists, its weight is updated.

        Time: O(1)
        """
        # Ensure both vertices exist
        if node1 not in self._adjacency:
            self.add_vertex(node1)
        if node2 not in self._adjacency:
            self.add_vertex(node2)

        # Only count as new edge if it did not already exist
        is_new = node2 not in self._adjacency[node1]

        self._adjacency[node1][node2] = weight
        self._adjacency[node2][node1] = weight

        if is_new:
            self._edge_count += 1

    def get_neighbors(self, node):
        """Return a dictionary of {neighbor: weight} for the given node.

        Time: O(1) for dictionary lookup; returns a copy.

        Raises:
            KeyError: If the node does not exist.
        """
        if node not in self._adjacency:
            raise KeyError(f"Vertex '{node}' not found in graph")
        return dict(self._adjacency[node])

    def get_all_vertices(self):
        """Return a list of all vertices in the graph.

        Time: O(V)
        """
        return list(self._adjacency.keys())

    def get_all_edges(self):
        """Return a list of all unique edges as (node1, node2, weight) tuples.

        Each undirected edge is yielded only once using frozenset to
        deduplicate, which works with any hashable node types (strings,
        integers, mixed types, etc.).

        Time: O(E)
        """
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
        """Remove a vertex and all its incident edges from the graph.

        Time: O(V + E_v) where E_v is the number of edges incident to node.

        Raises:
            KeyError: If the node does not exist.
        """
        if node not in self._adjacency:
            raise KeyError(f"Vertex '{node}' not found in graph")

        # Remove all edges incident to this node
        for neighbor in list(self._adjacency[node].keys()):
            del self._adjacency[neighbor][node]
            self._edge_count -= 1

        # Remove the vertex itself
        del self._adjacency[node]
        self._vertex_count -= 1

    def remove_edge(self, node1, node2):
        """Remove the edge between node1 and node2.

        Time: O(1)

        Raises:
            KeyError: If either node or the edge does not exist.
        """
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
        """Return the number of vertices in the graph.

        Time: O(1)
        """
        return self._vertex_count

    def edge_count(self):
        """Return the number of edges in the graph.

        Time: O(1)
        """
        return self._edge_count

    def __str__(self):
        """Return a string representation of the graph."""
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
        """Return a detailed string representation."""
        return f"Graph(vertices={self._vertex_count}, edges={self._edge_count})"
