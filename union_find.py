class UnionFind:

    def __init__(self):
        self._parent = {}
        self._rank = {}

    def make_set(self, node):
        if node not in self._parent:
            self._parent[node] = node
            self._rank[node] = 0

    def find(self, node):
        if node not in self._parent:
            raise KeyError(f"Node '{node}' has not been added to UnionFind")

        if self._parent[node] != node:
            self._parent[node] = self.find(self._parent[node])
        return self._parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return

        if self._rank[root1] < self._rank[root2]:
            self._parent[root1] = root2
        elif self._rank[root1] > self._rank[root2]:
            self._parent[root2] = root1
        else:
            self._parent[root2] = root1
            self._rank[root1] += 1

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)

    def __str__(self):
        sets = {}
        for node in self._parent:
            root = self.find(node)
            if root not in sets:
                sets[root] = []
            sets[root].append(node)
        return f"UnionFind({dict(sets)})"

    def __repr__(self):
        return f"UnionFind(sets={self._parent})"
