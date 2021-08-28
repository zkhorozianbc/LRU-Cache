from lru_cache import LRUCache
from node import Node
from linked_list import LL

def test_ll():
    l = LL()

    n1 = Node(1,1)
    n2 = Node(2,2)
    n3 = Node(3,3)
    n4 = Node(4,4)
    l.push(n1)
    l.push(n2)
    l.push(n3)
    l.push(n4)
    l.pop(1)
    l.push(n1)
    l.print_forward()
    l.print_reverse()


def get_test_ll():
    ll = LL()
    n1 = Node(1,1)
    n2 = Node(2,2)
    n3 = Node(3,3)
    n4 = Node(4,4)
    ll.push(n1)
    ll.push(n2)
    ll.push(n3)
    ll.push(n4)
    return ll



def test():
    ops = ["LRUCache","put","put","get","put","put","get"]
    vals = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    lru_cache = None
    answers = []
    for i in range(len(ops)):
        ans = None
        if i == 0:
            lru_cache = LRUCache(vals[i][0])
        elif ops[i] == "get" and len(vals[i]) == 1:
            ans = lru_cache.get(vals[i][0])
        elif ops[i] == "put" and len(vals[i]) == 2:
            ans = lru_cache.put(vals[i][0],vals[i][1])
        else:
            raise Exception(f"Bad input at index {i}")
        answers.append(ans)
        lru_cache.ll.print_forward()

    print(answers)

if __name__ == "__main__":
    test()
