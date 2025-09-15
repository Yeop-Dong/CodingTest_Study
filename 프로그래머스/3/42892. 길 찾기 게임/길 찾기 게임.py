import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self, key, value, left = None, right = None):
        self._key = key
        self._value = value
        self._left = left
        self._right = right

    def insert(self, key, value):
        if key < self._key:
            if self._left: 
                self._left.insert(key, value)
            else:
                self._left = Node(key, value)
        else:
            if self._right:
                self._right.insert(key, value)
            else:
                self._right = Node(key, value)
    def preorder(self):
        trav = [self._value]
        if self._left:
            trav += self._left.preorder()
        if self._right:
            trav += self._right.preorder()
        return trav
    def postorder(self):
        trav = []
        if self._left:
            trav += self._left.postorder()
        if self._right:
            trav += self._right.postorder()
        trav += [self._value]
        return trav
        
def solution(nodeinfo):
    answer = [[]]
    nodeinfo = [ (x, y, i+1) for i, (x, y) in enumerate(nodeinfo)  ]
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    root = Node(nodeinfo[0][0], nodeinfo[0][2])
    for x, y, i in nodeinfo[1:]:
        root.insert(x, i)
    return [root.preorder(), root.postorder()]
    