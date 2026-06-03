import unittest
from app.data_structures import Graph
from app.algorithms.bfs import bfs, is_connected_bfs
from app.algorithms.dfs import dfs, is_connected_dfs
from app.algorithms.kruskal import kruskal


class TestAlgorithms(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_bfs_dfs_empty_graph(self):
        # Empty graph connectivity
        res_bfs = is_connected_bfs(self.graph)
        self.assertTrue(res_bfs["is_connected"])
        self.assertEqual(res_bfs["total_vertices"], 0)

        res_dfs = is_connected_dfs(self.graph)
        self.assertTrue(res_dfs["is_connected"])
        self.assertEqual(res_dfs["total_vertices"], 0)

    def test_bfs_dfs_connected_graph(self):
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("B", "C", 2.0)
        self.graph.add_edge("C", "D", 1.5)

        # BFS connectivity
        res_bfs = is_connected_bfs(self.graph)
        self.assertTrue(res_bfs["is_connected"])
        self.assertEqual(res_bfs["total_vertices"], 4)
        self.assertEqual(res_bfs["visited_count"], 4)

        # DFS connectivity
        res_dfs = is_connected_dfs(self.graph)
        self.assertTrue(res_dfs["is_connected"])
        self.assertEqual(res_dfs["total_vertices"], 4)
        self.assertEqual(res_dfs["visited_count"], 4)

    def test_bfs_dfs_disconnected_graph(self):
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("C", "D", 2.0)

        # BFS connectivity
        res_bfs = is_connected_bfs(self.graph)
        self.assertFalse(res_bfs["is_connected"])
        self.assertEqual(res_bfs["total_vertices"], 4)
        self.assertEqual(res_bfs["visited_count"], 2)

        # DFS connectivity
        res_dfs = is_connected_dfs(self.graph)
        self.assertFalse(res_dfs["is_connected"])
        self.assertEqual(res_dfs["total_vertices"], 4)
        self.assertEqual(res_dfs["visited_count"], 2)

    def test_kruskal_empty_graph(self):
        result = kruskal(self.graph)
        self.assertEqual(result["edges"], [])
        self.assertEqual(result["total_cost"], 0.0)
        self.assertEqual(result["edge_count"], 0)
        self.assertFalse(result["is_complete"])

    def test_kruskal_single_node(self):
        self.graph.add_vertex("A")
        result = kruskal(self.graph)
        self.assertEqual(result["edges"], [])
        self.assertEqual(result["total_cost"], 0.0)
        self.assertEqual(result["edge_count"], 0)
        self.assertTrue(result["is_complete"])

    def test_kruskal_standard_mst(self):
        # Create a simple graph
        # A --(1)-- B
        # B --(2)-- C
        # A --(3)-- C
        # C --(4)-- D
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("B", "C", 2.0)
        self.graph.add_edge("A", "C", 3.0)
        self.graph.add_edge("C", "D", 4.0)

        result = kruskal(self.graph)
        self.assertTrue(result["is_complete"])
        self.assertEqual(result["total_cost"], 7.0)
        self.assertEqual(result["edge_count"], 3)
        
        # Verify specific edges chosen in MST: (A, B, 1.0), (B, C, 2.0), (C, D, 4.0)
        mst_edges = sorted(result["edges"], key=lambda x: x[2])
        self.assertEqual(mst_edges[0][2], 1.0)
        self.assertEqual(mst_edges[1][2], 2.0)
        self.assertEqual(mst_edges[2][2], 4.0)

    def test_kruskal_disconnected_graph(self):
        # A --(1)-- B
        # C --(2)-- D
        # Disconnected graph should compute spanning forest and set is_complete to False
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("C", "D", 2.0)

        result = kruskal(self.graph)
        self.assertFalse(result["is_complete"])
        self.assertEqual(result["total_cost"], 3.0)
        self.assertEqual(result["edge_count"], 2)


if __name__ == "__main__":
    unittest.main()
