from .node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self._length = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    def insert(self, val):
        """
        """
        # node = Node(val)
        # node._next = self.head
        # self.head = node

        self.head = Node(val, self.head)
        self._length += 1

        return self.head.val

    def includes(self, val):
        """
        """
        current = self.head

        while current is not None:
            if current.val == val:
                return True
            current = current._next

        return False
