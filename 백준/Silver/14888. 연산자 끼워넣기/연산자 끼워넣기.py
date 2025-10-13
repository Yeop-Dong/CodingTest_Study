n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
global maximum, minimum
INF = 1000000001
maximum = -INF
minimum = INF
def calc(p, m, mul, d, cur = nums[0], i = 1):
    global maximum, minimum
    if i == len(nums):
        maximum = max(maximum, cur)
        minimum = min(minimum, cur)
    if p > 0:
        calc(p - 1, m, mul, d, cur + nums[i], i + 1)
    if m > 0:
        calc(p, m - 1, mul, d, cur - nums[i], i + 1)
    if mul > 0:
        calc(p, m, mul - 1, d, cur * nums[i], i + 1)
    if d > 0:
        ncur = cur // nums[i]
        if cur < 0:
            ncur = (-cur) // nums[i]
            ncur = -ncur
        calc(p, m, mul, d - 1, ncur, i + 1)  
calc(plus, minus, multiply, divide)
print(maximum)
print(minimum)