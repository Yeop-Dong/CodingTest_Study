s = input()
bomb = input()[::-1]
def bmbchk(st):
    if len(st) < len(bomb):
        return False
    for i in range(1, len(bomb) + 1):
        if st[-i] != bomb[i - 1]:
            return False
    return True
st = []
for c in s:
    st.append(c)
    if c == bomb[0]:
        if bmbchk(st):
            for _ in range(len(bomb)):
                st.pop()
result = ''.join(st)
print(result if result else "FRULA")