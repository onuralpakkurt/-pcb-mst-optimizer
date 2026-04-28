"""
Queue (FIFO) Data Structure

Implementation using a singly linked list so that both enqueue and dequeue
are O(1). A Node class is defined inside this file for internal use.

Time Complexities:
    enqueue(item): O(1) — insert at tail via tail pointer
    dequeue():     O(1) — remove from head
    peek():        O(1) — read head value
    is_empty():    O(1) — check head is None
    size():        O(1) — return stored counter
"""


class _Node:
    """Internal node for the singly linked list used by Queue."""

    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """A First-In-First-Out (FIFO) queue implementation."""

    def __init__(self):
        """Initialize an empty queue."""
        self._head = None  # front of the queue (dequeue from here)
        self._tail = None  # back of the queue  (enqueue to here)
        self._size = 0

    def enqueue(self, item):
        """Add an item to the back of the queue.

        Time: O(1)
        """
        new_node = _Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the item at the front of the queue.

        Time: O(1)

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self):
        """Return the front item without removing it.

        Time: O(1)

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self):
        """Return True if the queue is empty, False otherwise.

        Time: O(1)
        """
        return self._head is None

    def size(self):
        """Return the number of items in the queue.

        Time: O(1)
        """
        return self._size

    def __str__(self):
        """Return a string representation of the queue."""
        items = []
        current = self._head
        while current is not None:
            items.append(current.value)
            current = current.next
        return f"Queue({items})"

    def __repr__(self):
        """Return a detailed string representation."""
        items = []
        current = self._head
