from collections import deque

def solution(rc, operations):
    r, c = len(rc), len(rc[0])
    mid = deque([ deque(row[1:c-1]) for row in rc ])
    left, right = deque([row[0] for row in rc]), deque([row[-1] for row in rc])
    def ShiftRow():
        mid.rotate(1)
        left.rotate(1)
        right.rotate(1)
    def Rotate():
        mid[0].appendleft(left.popleft())
        right.appendleft(mid[0].pop())
        mid[-1].append(right.pop())
        left.append(mid[-1].popleft())
    for op in operations:
        locals()[op]()
    for i in range(r):
        mid[i].appendleft(left.popleft())
        mid[i].append(right.popleft())
    return [ list(row) for row in mid ]