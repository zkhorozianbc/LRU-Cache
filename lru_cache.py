from typing import Optional
from linked_list import LL
from node import Node


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ll = LL()

    def get(self, key: int) -> int:

        n = self.ll.pop(key)
        if n is None:
            return -1
        self.ll.push(n)
        return n.val

    def put(self, key: int, value  : int) -> None:

        n = self.ll.pop(key)
        if n is not None:
            n.val = value
            self.ll.push(n)
            return

        new_node = Node(key,value)
        if self.ll.size() == self.capacity:
            self.ll.pop_head()

        self.ll.push(new_node)
