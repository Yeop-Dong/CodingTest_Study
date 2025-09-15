N = int(input())
for i in range(1, 1000000):
    if 3 * (i - 1) * i + 1 >= N:
        print(i)
        break