from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self):
        self.head: Node = None
        self._length: int = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length

    # def __iter__(self):
    #     pass
    #
    # def __next__(self):
    #     pass

    def insert(self, val: Any) -> Node:
        pass

    # def includes(self, val: str, data: int) -> bool:
    def includes(self, val: Any) -> bool:
        pass
