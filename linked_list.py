from typing import Optional
from node import Node


class LL:
    """
    Full implementation of doubly linked list

    """
    def __init__(self):
        self.head = None #type: Optional[Node]
        self.tail = self.head #type: Optional[Node]
        self.ref_map = {} #type: Dict[str,Node]


    def size(self):
        """
        Returns current size of linked list by taking length of ref_map
        """
        return len(self.ref_map)


    def get(self,key: int) -> Optional[Node]:
        """
        Get but don't pop node in list. Return None if doesn't exist
        """
        if key not in self.ref_map:
            return None
        return self.ref_map[key]


    def push(self,n : Node) -> None:
        """
        Add new Node n to end of list.
        """
        #save reference to tail
        prev_tail = self.tail

        n.prev = prev_tail
        #set tail ref to n
        self.tail = n
        #set previous tail next ref to new tail
        #or set head ref to new tail
        if prev_tail is not None:
            prev_tail.next = self.tail
        else:
            self.head = self.tail

        #update ref map with n
        self.ref_map[n.key] = n

    def pop(self, key: int) -> Optional[Node]:
        """
        Remove node from list with specified key
        """
        #if key not in ref map, then node is not in list
        #return None
        n = self.get(key)
        if n is None:
            return None

        prev_node = n.prev
        next_node = n.next

        #set prev_node's next ref to next node
        #or set head to next_node if n is head (i.e. prev_node is None)
        if prev_node is None:
            self.head = next_node
        else:
            prev_node.next = next_node

        #set next_node's prev ref to prev_node
        #or set tail ref to prev_node if n is tail (i.e. next_node is None)
        if next_node is None:
            self.tail = prev_node
        else:
            next_node.prev = prev_node

        #delete n from ref map
        del self.ref_map[key]

        n.next = None
        n.prev = None

        return n

    def pop_head(self) -> None:
        if self.head is not None:
            self.pop(self.head.key)


    def __str__(self) -> str:
        s = ""
        s += "Linked List:\n"
        trav = self.head
        while trav is not None:
            s += str(trav)
            trav = trav.next
        s += "---------"
        return s
    def print(self) -> str:
        print("Linked List:")
        trav = self.head
        while trav is not None:
            print(str(trav))
            trav = trav.next
        print("---------")


    def print_reverse(self):
        print("Linked List in Reverse:")
        trav = self.tail
        while trav is not None:
            print(str(trav))
            trav = trav.prev
        print("---------")
