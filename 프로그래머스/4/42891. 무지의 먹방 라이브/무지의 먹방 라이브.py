def solution(food_times, k):
    answer = 0
    food_times = [ (i+1, f) for i, f in enumerate(food_times) ]
    food_times.sort(key = lambda x: x[1])
    cur = 0
    last = 0
    while cur < len(food_times):
        finished = food_times[cur][1] - last
        cycle = len(food_times) - cur
        finish_dish = cycle * finished
        if finish_dish > k:
            break
        k -= finish_dish
        last = food_times[cur][1]
        cur += 1
    if cur == len(food_times):
        return -1
    food_times = food_times[cur:]
    food_times.sort(key = lambda x: x[0])
    cycle = len(food_times)
    return food_times[k % cycle][0]