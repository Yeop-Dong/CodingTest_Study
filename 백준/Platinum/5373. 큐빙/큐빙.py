from collections import deque
colors = { "U":"w","D":"y","F":"r","B":"o","R":"b","L":"g" }
rotateinfo = {
    "U": "B0 B1 B2 R0 R1 R2 F0 F1 F2 L0 L1 L2",
    "D": "F6 F7 F8 R6 R7 R8 B6 B7 B8 L6 L7 L8",
    "F": "U6 U7 U8 R0 R3 R6 D2 D1 D0 L8 L5 L2",
    "B": "U2 U1 U0 L0 L3 L6 D6 D7 D8 R8 R5 R2",
    "L": "U0 U3 U6 F0 F3 F6 D0 D3 D6 B8 B5 B2",
    "R": "U8 U5 U2 B0 B3 B6 D8 D5 D2 F8 F5 F2"
}
rotates = {}
for r, item in rotateinfo.items():
    tokens = item.split()
    seq = []
    for t in tokens:
        face, idx = t[0], int(t[1])
        seq.append((face, idx))
    rotates[r] = seq
def rotate_face(face, way):
    if way == '+':  # 시계 방향
        cube[face] = [cube[face][6], cube[face][3], cube[face][0],
                      cube[face][7], cube[face][4], cube[face][1],
                      cube[face][8], cube[face][5], cube[face][2]]
    else:  # 반시계 방향
        cube[face] = [cube[face][2], cube[face][5], cube[face][8],
                      cube[face][1], cube[face][4], cube[face][7],
                      cube[face][0], cube[face][3], cube[face][6]]
def rotate(face, way):
    rotate_face(face, way)
    seq = rotates[face]
    temp = [cube[f][i] for f, i in seq]
    dq = deque(temp)
    dq.rotate(3 if way == '+' else -3)
    for (f, i), c in zip(seq, dq):
        cube[f][i] = c
t = int(input())
for _ in range(t):
    cube = {f: [c]*9 for f, c in colors.items()}
    n = int(input())
    cmds = input().split()
    for cmd in cmds:
        rotate(cmd[0], cmd[1])
    print(''.join(cube['U'][:3]))
    print(''.join(cube['U'][3:6]))
    print(''.join(cube['U'][6:9]))