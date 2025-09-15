s = input()
t = input()
ls = len(s)
def game(cur):
    if cur == s:
        return True
    if len(cur) == ls:
        return False
    result = False
    if cur[0] == "B":
        result = result or game(cur[1:][::-1])
    if cur[-1] == "A":
        result = result or game(cur[:-1])
    return result
    
g = game(t)
print(1 if g else 0)