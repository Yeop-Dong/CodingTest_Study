N = int(input())
ch =[]
for _ in range(N):
    ch.append(input())
for i, c in enumerate(ch):
    if c == "KBS1":
        c1 = i
    elif c == "KBS2":
        c2 = i
answer = ""
answer += "1" * c1 + "4" * c1
if c1 > c2:
    c2 += 1
answer += "1" * c2 + "4" * (c2 - 1)
print(answer)