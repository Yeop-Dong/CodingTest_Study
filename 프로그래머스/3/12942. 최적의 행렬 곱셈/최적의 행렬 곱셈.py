import itertools
def solution(matrix_sizes):
    answer = 0
    N = len(matrix_sizes)
    DP = [ [ 0 if i == j else 2e10 for i in range(N) ] for j in range(N) ]
    
    for i in range(N):
        for a in range(N - i):
            b = a + i
            for k in range(a, b):
                after = matrix_sizes[a][0] * matrix_sizes[k][1] * matrix_sizes[b][1]
                DP[a][b] = min(DP[a][b], DP[a][k] + DP[k+1][b] + after)
    answer = DP[0][N-1]    
    return answer