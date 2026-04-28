class _Node:
    __slots__ = ("value", "next")

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        new_node = _Node(item)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self._head.value
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._head.value

    def is_empty(self):
        return self._head is None

    def size(self):
        return self._size

    def __str__(self):
        items = []
        current = self._head
        while current is not None:
            items.append(current.value)
            current = current.next
        return f"Queue({items})"

    def __repr__(self):
        items = []
        current = self._head
        while current is not None:
            items.append(current.value)
            current = current.next
        return f"Queue({items})"
