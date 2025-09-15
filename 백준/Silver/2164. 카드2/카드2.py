from collections import deque

n = int(input())
card = deque([i+1 for i in range(n)])

while len(card) > 2:
    card.popleft()
    card.rotate(-1)
last = card[0] if len(card) == 1 else card[1]
print(last)