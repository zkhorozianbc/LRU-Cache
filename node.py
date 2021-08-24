from typing import Optional

class Node:
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val
        self.prev = None #type: Optional[Node]
        self.next = None #type: Optional[Node]
    def __str__(self) -> str:
        return f"Node: key {self.key}, val {self.val}\n"
