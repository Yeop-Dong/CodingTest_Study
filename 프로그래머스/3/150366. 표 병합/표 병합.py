def solution(commands):
    answer = []
    table = [ [ (r, c, 0) for c in range(51) ] for r in range(51) ]
    values = [ "EMPTY" ]
    
    def find(r, c):
        nr, nc, _ = table[r][c]
        if (nr, nc) != (r, c):
            return find(nr, nc)
        return (r, c)
    def union(r1, c1, r2, c2):
        r1, c1 = find(r1, c1)
        r2, c2 = find(r2, c2)
        if r1 == r2 and c1 == c2:
            return
        
        v1 = table[r1][c1][2]
        v2 = table[r2][c2][2]
        if v1 == 0:
            table[r1][c1] = (r2, c2, 0)
        else:
            table[r2][c2] = (r1, c1, 0)
        
        
    for cmd in commands:
        cmds = cmd.split()
        typ = cmds[0]
        if typ == "UPDATE":
            if len(cmds) == 4:
                r, c, value = int(cmds[1]), int(cmds[2]), cmds[3]
                rr, rc = find(r, c)
                try:
                    idx = values.index(value)
                except:
                    values.append(value)
                    idx = len(values) - 1
                table[rr][rc] = (rr, rc, idx)
            if len(cmds) == 3:
                value1, value2 = cmds[1:]
                try:
                    idx = values.index(value1)
                except:
                    continue
                values[idx] = value2
        if typ == "MERGE":
            r1, c1, r2, c2 = map(int, cmds[1:])
            union(r1, c1, r2, c2)
        if typ == "UNMERGE":
            r, c = map(int, cmds[1:])
            root_r, root_c = find(r, c)
            vidx = table[root_r][root_c][2]
            friends = []
            for i in range(1, 51):
                for j in range(1, 51):
                    if (root_r, root_c) == find(i, j):
                        friends.append((i, j))
            for i, j in friends:
                table[i][j] = i, j, 0
            table[r][c] = (r, c, vidx)
        if typ == "PRINT":
            r, c = map(int, cmds[1:])
            r, c = find(r, c)
            vidx = table[r][c][2]
            answer.append(values[vidx])
        
                
    return answer