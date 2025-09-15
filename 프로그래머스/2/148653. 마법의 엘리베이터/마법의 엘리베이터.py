def solution(storey):
    if (storey == 0):
        return 0
    digit = storey % 10
    print(storey, digit)
    if digit > 5:
        return 10 - digit + solution(storey // 10 + 1)
    if digit == 5:
        if storey // 10 % 10 >= 5:
            return 10 - digit + solution(storey // 10 + 1)
        else:
            return digit + solution(storey // 10)
    return digit + solution(storey // 10)