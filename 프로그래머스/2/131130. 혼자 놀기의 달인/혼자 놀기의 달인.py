def solution(cards):
    groups = []
    for c in cards:
        if not any(c in group for group in groups):
            boxes = [c]
            nxt = cards[c - 1]
            while nxt not in boxes:
                boxes.append(nxt)
                nxt = cards[nxt - 1]
            groups.append(boxes)
    groups.sort(key=len, reverse=True)
    if len(groups) == 1:
        return 0
    else:
        return len(groups[0]) * len(groups[1])