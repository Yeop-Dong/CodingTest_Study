
def solution(beginning, target):
    answer = 0
    height, width = len(target), len(target[0])
    count_bit = lambda x: bin(x).count('1')
    answer = height + width + 1
    for h in range(1 << height):
        for w in range(1 << width):
            for i in range(height):
                for j in range(width):
                    if target[i][j] != beginning[i][j] ^ h >> i & 1 ^ w >> j & 1:
                        break
                else:
                    continue
                break
            else:
                answer = min(answer, count_bit(h) + count_bit(w))
    return answer if answer != height + width + 1 else -1