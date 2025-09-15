from collections import deque
n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([False] * n)
cnt = 0
def chkbot():
    robot[n - 1] = False
def rotate():
    a.rotate()
    robot.rotate()
    chkbot()
def movebot():
    for i in range(n - 1, -1, -1):
        if robot[i]:
            if a[i+1] > 0 and not robot[i+1]:
                robot[i] = False
                robot[i+1] = True
                a[i+1] -= 1
    chkbot()
def putbot():
    if not robot[0] and a[0] > 0:
        robot[0] = True
        a[0] -= 1
while a.count(0) < k:
    cnt += 1
    rotate()
    movebot()
    putbot()
print(cnt)