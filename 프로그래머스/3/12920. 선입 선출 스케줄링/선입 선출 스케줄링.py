import math
import functools
def solution(n, cores):
    l = 0
    size = len(cores)
    r = 500000001
    while l < r:
        mid = (l + r) // 2
        result = functools.reduce(lambda acc, c: mid // c + acc, cores, size)
        if result < n:
            l = mid + 1
        else:
            r = mid
    
    done = functools.reduce(lambda acc, c: r // c + acc, cores, size)
    for i in range(size-1, -1, -1):
        if l % cores[i] == 0:
            done -= 1
            if done == n - 1:
                return i + 1