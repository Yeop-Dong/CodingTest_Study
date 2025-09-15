from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(k, room_number):
    answer = []
    room = defaultdict(int)
    def find_room(num):
        if not room[num]:
            room[num]=num+1
            return num
        room[num] = find_room(room[num])
        return room[num]
    for n in room_number:
        answer.append(find_room(n))
    return answer