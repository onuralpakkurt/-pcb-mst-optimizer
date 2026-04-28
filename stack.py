"""
Stack (LIFO) Data Structure

Implementation using a plain Python list.

Time Complexities:
    push(item): O(1) — amortized append to end of list
    pop():      O(1) — pop from end of list
    peek():     O(1) — index lookup of last element
    is_empty(): O(1) — compare size to zero
    size():     O(1) — return stored length
"""


class Stack:
    """A Last-In-First-Out (LIFO) stack implementation."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Push an item onto the top of the stack.

        Time: O(1) amortized
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the top item from the stack.

        Time: O(1)

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it.

        Time: O(1)

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise.

        Time: O(1)
        """
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack.

        Time: O(1)
        """
        return len(self._items)

    def __str__(self):
        """Return a string representation of the stack."""
        return f"Stack({self._items})"

    def __repr__(self):
        """Return a detailed string representation."""
        return f"Stack({self._items})"
