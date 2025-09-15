def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    affect = [ [0] * (m+1) for _ in range(n+1) ]
    
    for typ, r1, c1, r2, c2, degree in skill:
        if typ == 1:
            degree = -degree
        affect[r1][c1] += degree
        affect[r2+1][c2+1] += degree
        affect[r1][c2+1] -= degree
        affect[r2+1][c1] -= degree
    for i in range(n):
        for j in range(1, m+1):
            affect[i][j] = affect[i][j-1] + affect[i][j]
    for j in range(m):
        for i in range(1, n+1):
            affect[i][j] = affect[i-1][j] + affect[i][j]
    for i in range(n):
        for j in range(m):
            board[i][j] = board[i][j] + affect[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer