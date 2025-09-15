import sys
n, m = map(int, input().split())
word = [ sys.stdin.readline().rstrip('\n') for _ in range(n)]
words={}
for w in word:
    if len(w) < m: continue
    words[w] = words.get(w, 0) + 1
word = [(words[w], len(w), w) for w in words]
word.sort(key = lambda x: (-x[0], -x[1], x[2]))
for _, _, w in word:
    print(w)