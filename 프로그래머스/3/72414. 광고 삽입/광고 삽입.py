def solution(play_time, adv_time, logs):
    answer = ''
    def ttos(time):
        h, m, s = int(time[:2]), int(time[3:5]), int(time[6:8])
        return h * 3600 + m * 60 + s
    def stot(sec):
        h = sec // 3600
        m = sec % 3600 // 60
        s = sec % 60
        return f'{h:02d}:{m:02d}:{s:02d}'
    play_sec = ttos(play_time)
    dur = ttos(adv_time)
    
    cumulative = [ 0 for _ in range(play_sec + 1)]
    for l in logs:
        start, end = ttos(l[:8]), ttos(l[9:])
        cumulative[start] += 1
        cumulative[end] -= 1
    
    max_cumul = -1
    max_abegin = -1
    
    for i in range(1, play_sec + 1):
        cumulative[i] = cumulative[i] + cumulative[i-1]
    for i in range(1, play_sec + 1):
        cumulative[i] = cumulative[i] + cumulative[i-1]
    max_cumul = cumulative[dur - 1]
    max_abegin = 0
    for i in range(1, play_sec - dur + 2):
        cumul = cumulative[i + dur - 1] - cumulative[i-1]
        if max_cumul < cumul:
            max_cumul = cumul
            max_abegin = i
            
    return stot(max_abegin)