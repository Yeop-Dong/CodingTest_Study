def to_binary(number):
    if number == 0:
        return ""
    return to_binary(number // 2) + str(number % 2)
def calc_height(binary):
    h = 1
    while len(binary) > pow(2, h) - 1:
        h += 1
    return h
def check(binary, last = '1'):
    mid = len(binary) // 2
    val = binary[mid]
    
    if last == '0' and val == '1':
        return False
    
    if len(binary) == 1:
        return True
    
    return check(binary[:mid], val) and check(binary[mid+1:], val)
        
    
def solution(numbers):
    answer = []
    
    for n in numbers:
        binary = to_binary(n)
        h = calc_height(binary)
        diff = pow(2, h) - 1 - len(binary)
        if diff > 0:
            binary = "0" * diff + binary
        chk = 1 if check(binary) else 0
        answer.append(chk)

    return answer