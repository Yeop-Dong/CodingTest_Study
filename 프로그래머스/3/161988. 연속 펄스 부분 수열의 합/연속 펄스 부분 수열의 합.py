pulse = [[0] * 500001] * 2
def solution(sequence):
    pulse[0][0] = sequence[0]
    pulse[1][0] = -sequence[0]
    sign = -1
    for i in range(1, len(sequence)):
        pulse[0][i] = pulse[0][i-1] + sign * sequence[i]
        sign *= -1
        pulse[1][i] = pulse[0][i-1] + sign * sequence[i]
        
    return max( max(pulse[1]) - min(pulse[1]), max(pulse[0]) - min(pulse[0]) )
    