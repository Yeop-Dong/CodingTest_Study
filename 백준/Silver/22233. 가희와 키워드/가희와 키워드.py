import sys
input = lambda: sys.stdin.readline().rstrip()
output = lambda x: sys.stdout.write(x)
n, m = map(int, input().split())
keywords = {}
for _ in range(n):
    keyword = input()
    keywords[keyword] = True
cnt = len(keywords)
out = []
for _ in range(m):
    words = input().split(',')
    for w in words:
        if keywords.get(w, False):      
            keywords[w] = False
            cnt -= 1
    out.append(str(cnt))
print('\n'.join(out))