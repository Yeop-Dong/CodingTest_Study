def solution(coin, cards):
    answer = 1
    n = len(cards)
    hand, deck = cards[:n // 3], cards[n // 3:][::-1]
    hand = set(hand)
    draw = set()
    while deck:
        flag = False
        draw.add(deck.pop())
        draw.add(deck.pop())
        for c in hand:
            op = n + 1 - c
            if op in hand:
                hand.remove(c)
                hand.remove(op)
                break
        else:
            flag = True    
        if flag and coin >= 1 and hand and draw:
            flag = False
            for c in hand:
                op = n + 1 - c
                if op in draw:
                    hand.remove(c)
                    draw.remove(op)
                    coin -= 1
                    break
            else:
                flag = True
        if flag and coin >= 2 and draw:
            flag = False
            for c in draw:
                op = n + 1 - c
                if op in draw:
                    draw.remove(c)
                    draw.remove(op)
                    coin -= 2
                    break
            else:
                flag = True
        if flag:
            break
        answer += 1
    return answer