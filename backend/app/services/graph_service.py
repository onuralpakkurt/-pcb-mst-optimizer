import asyncio

from app.data_structures import Graph


class GraphService:
    def __init__(self):
        self._graph = Graph()
        self._lock = asyncio.Lock()

    async def reset(self):
        async with self._lock:
            self._graph = Graph()
            return self._graph

    async def add_node(self, node_id: str) -> int:
        async with self._lock:
            self._graph.add_vertex(node_id)
            return self._graph.vertex_count()

    async def add_edge(self, from_node: str, to_node: str, weight: float) -> int:
        async with self._lock:
            self._graph.add_edge(from_node, to_node, weight)
            return self._graph.edge_count()

    def get_graph(self) -> Graph:
        return self._graph


graph_service = GraphService()
