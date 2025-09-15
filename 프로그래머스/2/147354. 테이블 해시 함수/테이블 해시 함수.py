
def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    slist = []
    for i in range(row_begin - 1, row_end):
        sum = 0
        for d in data[i]:
            sum += d % (i + 1)
        slist.append(sum)
    hashed = slist[0]
    for i in range(1, len(slist)):
        hashed ^= slist[i]
    return hashed
    
    return answer