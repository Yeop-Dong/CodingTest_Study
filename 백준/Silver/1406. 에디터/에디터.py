from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()
print = sys.stdout.write
left, right = deque(input()), deque()
m = int(input())
for _ in range(m):
    cmd = input()
    if cmd.startswith('L'):
        if len(left):
            cursorL = left.pop()
            right.appendleft(cursorL)
    elif cmd.startswith('D'):
        if len(right):
            cursorR = right.popleft()
            left.append(cursorR)
    elif cmd.startswith('B'):
        if len(left):
            left.pop()
    elif cmd.startswith('P'):
        ch = cmd.split()[1]
        left.append(ch)
while left:
    print(left.popleft())
while right:
    print(right.popleft())