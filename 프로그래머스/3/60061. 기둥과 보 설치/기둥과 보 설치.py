from collections import defaultdict

def solution(n, build_frame):
    pillar, beam = defaultdict(bool), defaultdict(bool)
    
    def check(x, y, a, b):
        def check_pillar(x, y, p, b):
            if y == 0:
                return True
            elif (x, y) in b or (x-1, y) in b:
                return True
            elif (x, y-1) in p:
                return True
            return False
        def check_beam(x, y, p, b):
            if (x, y-1) in p or (x+1, y-1) in p:
                return True
            if (x-1, y) in b and (x+1, y) in b:
                return True
            return False
        
        if a == 0:
            if b == 1:
                return check_pillar(x, y, pillar, beam)
            if b == 0:
                pillar_copy = pillar.copy()
                pillar_copy.pop((x, y))
                for (x, y) in pillar_copy:
                    if not check_pillar(x, y, pillar_copy, beam):
                        return False
                for (x, y) in beam:
                    if not check_beam(x, y, pillar_copy, beam):
                        return False
        else:
            if b == 1:
                return check_beam(x, y, pillar, beam)
            if b == 0:
                beam_copy = beam.copy()
                beam_copy.pop((x, y))
                for (x, y) in pillar:
                    if not check_pillar(x, y, pillar, beam_copy):
                        return False
                for (x, y) in beam_copy:
                    if not check_beam(x, y, pillar, beam_copy):
                        return False
        return True
                    
    for x, y, a, b in build_frame:
        if check(x, y, a, b):
            if a == 0:
                if b == 1:
                    pillar[(x, y)] = True
                else:
                    pillar.pop((x, y))
            elif b == 1:
                beam[(x, y)] = True
            else:
                beam.pop((x, y))
        
    answer = []
    for i in range(n+1):
        for j in range(n+1):
            if (i, j) in pillar:
                answer.append([i, j, 0])
            if (i, j) in beam:
                answer.append([i, j, 1])
    return answer