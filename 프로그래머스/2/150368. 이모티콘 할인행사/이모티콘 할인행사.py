def calc(users, emoticons, discounts):
    sub, sale = 0, 0
    for user in users:
        cur = 0
        for i in range(len(emoticons)):
            if user[0] <= discounts[i]:
                cur += emoticons[i] // 100 * (100 - discounts[i])
        if user[1] <= cur:
            sub += 1
        else:
            sale += cur
    return sub, sale

def dfs(rates, users, emoticons, discounts):
    best_sub, best_sale = 0, 0
    if len(discounts) == len(emoticons):
        best_sub, best_sale = calc(users, emoticons, discounts)
        return best_sub, best_sale
    
    for r in rates:
        sub, sale = dfs(rates, users, emoticons, discounts + [r])
        if best_sub < sub:
            best_sub, best_sale = sub, sale
        elif best_sub == sub and best_sale <= sale:
            best_sale = sale
    return best_sub, best_sale
    
def solution(users, emoticons):
    rates = [10, 20, 30, 40]
    best_sub, best_sale = dfs(rates, users, emoticons, [])
    return [best_sub, best_sale]