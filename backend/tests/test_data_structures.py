import unittest
from app.data_structures import Graph, UnionFind, Queue, Stack


class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_initial_state(self):
        self.assertEqual(self.graph.vertex_count(), 0)
        self.assertEqual(self.graph.edge_count(), 0)
        self.assertEqual(self.graph.get_all_vertices(), [])
        self.assertEqual(self.graph.get_all_edges(), [])

    def test_add_vertex(self):
        self.graph.add_vertex("A")
        self.assertEqual(self.graph.vertex_count(), 1)
        self.assertIn("A", self.graph.get_all_vertices())

        # Duplicate should not count twice
        self.graph.add_vertex("A")
        self.assertEqual(self.graph.vertex_count(), 1)

    def test_add_edge(self):
        self.graph.add_edge("A", "B", 4.5)
        self.assertEqual(self.graph.vertex_count(), 2)
        self.assertEqual(self.graph.edge_count(), 1)
        
        neighbors_A = self.graph.get_neighbors("A")
        self.assertIn("B", neighbors_A)
        self.assertEqual(neighbors_A["B"], 4.5)

        neighbors_B = self.graph.get_neighbors("B")
        self.assertIn("A", neighbors_B)
        self.assertEqual(neighbors_B["A"], 4.5)

        # Checking undirected representation
        edges = self.graph.get_all_edges()
        self.assertEqual(len(edges), 1)
        u, v, w = edges[0]
        self.assertTrue((u == "A" and v == "B") or (u == "B" and v == "A"))
        self.assertEqual(w, 4.5)

    def test_remove_edge(self):
        self.graph.add_edge("A", "B", 3.0)
        self.graph.remove_edge("A", "B")
        self.assertEqual(self.graph.edge_count(), 0)
        self.assertNotIn("B", self.graph.get_neighbors("A"))
        
        # Test error handling
        with self.assertRaises(KeyError):
            self.graph.remove_edge("A", "B")
        with self.assertRaises(KeyError):
            self.graph.remove_edge("A", "C")

    def test_remove_vertex(self):
        self.graph.add_edge("A", "B", 1.0)
        self.graph.add_edge("B", "C", 2.0)
        self.graph.remove_vertex("B")
        
        self.assertEqual(self.graph.vertex_count(), 2)
        self.assertEqual(self.graph.edge_count(), 0)
        self.assertNotIn("B", self.graph.get_all_vertices())
        
        with self.assertRaises(KeyError):
            self.graph.get_neighbors("B")
        with self.assertRaises(KeyError):
            self.graph.remove_vertex("B")

    def test_string_representation(self):
        self.graph.add_edge("A", "B", 1.5)
        self.assertTrue("Graph with 2 vertices" in str(self.graph))
        self.assertTrue("Graph(vertices=2, edges=1)" in repr(self.graph))


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.uf = UnionFind()

    def test_make_set_and_find(self):
        self.uf.make_set("A")
        self.uf.make_set("B")
        self.assertEqual(self.uf.find("A"), "A")
        self.assertEqual(self.uf.find("B"), "B")

        with self.assertRaises(KeyError):
            self.uf.find("C")

    def test_union_and_connected(self):
        self.uf.make_set("A")
        self.uf.make_set("B")
        self.uf.make_set("C")

        self.assertFalse(self.uf.connected("A", "B"))
        
        self.uf.union("A", "B")
        self.assertTrue(self.uf.connected("A", "B"))
        self.assertEqual(self.uf.find("A"), self.uf.find("B"))
        
        self.assertFalse(self.uf.connected("A", "C"))
        
        self.uf.union("B", "C")
        self.assertTrue(self.uf.connected("A", "C"))
        
    def test_rank_and_compression(self):
        elements = ["A", "B", "C", "D"]
        for el in elements:
            self.uf.make_set(el)
            
        self.uf.union("A", "B")
        self.uf.union("C", "D")
        self.uf.union("A", "C")
        
        # All elements should now belong to the same representative
        rep = self.uf.find("A")
        for el in elements:
            self.assertEqual(self.uf.find(el), rep)


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue_dequeue(self):
        self.assertTrue(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 0)

        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.size(), 3)
        self.assertEqual(self.queue.peek(), 1)

        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())

    def test_errors(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()
        with self.assertRaises(IndexError):
            self.queue.peek()


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_push_pop(self):
        self.assertTrue(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 0)

        self.stack.push("A")
        self.stack.push("B")
        self.stack.push("C")

        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.peek(), "C")

        self.assertEqual(self.stack.pop(), "C")
        self.assertEqual(self.stack.pop(), "B")
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.pop(), "A")
        self.assertTrue(self.stack.is_empty())

    def test_errors(self):
        with self.assertRaises(IndexError):
            self.stack.pop()
        with self.assertRaises(IndexError):
            self.stack.peek()


if __name__ == "__main__":
    unittest.main()
