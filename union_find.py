"""
Union-Find (Disjoint Set) Data Structure

Implementation with Path Compression and Union by Rank optimizations.

Time Complexities (all operations):
    make_set(node): O(1)
    find(node):     O(α(n)) — inverse Ackermann function (amortized)
    union(n1, n2):  O(α(n)) — amortized
    connected(n1, n2): O(α(n)) — amortized
"""


class UnionFind:
    """A disjoint-set data structure with path compression and union by rank."""

    def __init__(self):
        """Initialize an empty Union-Find structure."""
        self._parent = {}  # node -> parent node
        self._rank = {}    # node -> rank (upper bound on tree height)

    def make_set(self, node):
        """Create a new set containing only the given node.

        If the node already exists in the structure, this is a no-op.

        Time: O(1)
        """
        if node not in self._parent:
            self._parent[node] = node
            self._rank[node] = 0

    def find(self, node):
        """Find the representative (root) of the set containing node.

        Applies path compression: every node along the path is made to point
        directly to the root.

        Time: O(α(n)) amortized

        Raises:
            KeyError: If the node has not been added via make_set().
        """
        if node not in self._parent:
            raise KeyError(f"Node '{node}' has not been added to UnionFind")

        # Path compression
        if self._parent[node] != node:
            self._parent[node] = self.find(self._parent[node])
        return self._parent[node]

    def union(self, node1, node2):
        """Merge the sets containing node1 and node2.

        Uses union by rank: the tree with smaller rank is attached under
        the root of the larger rank.

        Time: O(α(n)) amortized

        Raises:
            KeyError: If either node has not been added via make_set().
        """
        root1 = self.find(node1)
        root2 = self.find(node2)

        # Already in the same set
        if root1 == root2:
            return

        # Union by rank: attach smaller rank tree under larger rank tree
        if self._rank[root1] < self._rank[root2]:
            self._parent[root1] = root2
        elif self._rank[root1] > self._rank[root2]:
            self._parent[root2] = root1
        else:
            # Ranks are equal; attach one under the other and increment rank
            self._parent[root2] = root1
            self._rank[root1] += 1

    def connected(self, node1, node2):
        """Return True if node1 and node2 belong to the same set.

        Time: O(α(n)) amortized

        Raises:
            KeyError: If either node has not been added via make_set().
        """
        return self.find(node1) == self.find(node2)

    def __str__(self):
        """Return a string representation showing each node's parent."""
        sets = {}
        for node in self._parent:
            root = self.find(node)
            if root not in sets:
                sets[root] = []
            sets[root].append(node)
        return f"UnionFind({dict(sets)})"

    def __repr__(self):
        """Return a detailed string representation."""
        return f"UnionFind(sets={self._parent})"
