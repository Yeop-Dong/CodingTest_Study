def solution(s):
    answer = []
    for x in s:
        cnt = 0
        c110 = 0
        result = ""
        for c in x:
            if c == '1':
                cnt += 1
            elif cnt > 1:
                cnt -= 2
                c110 += 1
            else:
                result += "1" * cnt + "0"
                cnt = 0
        result += "110" * c110 + "1" * cnt
        answer.append(result)
        
                
    return answer