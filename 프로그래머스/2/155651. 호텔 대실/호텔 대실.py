def strtotime(time_str):
    return int(time_str[:2]) * 60 + int(time_str[3:])

def solution(book_time):
    book_time.sort()
    book_time = [ [strtotime(s), strtotime(e)] for s, e in book_time ]
    room = {}
    max_size = 0
    idx = 0
    for b in book_time:
        bstart, bend = b
        keys = []
        for key, value in room.items():
            rstart, rend = value
            if bstart - rend >= 10:
                keys.append(key)
        for k in keys:
            del room[k]
        
        room[idx] = b
        idx += 1
        if max_size < len(room):
            max_size = len(room)
        
    return max_size