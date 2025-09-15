t = int(input())
for _ in range(t):
    n = int(input())
    def brute(cur: str = "1", i: int = 2):
        if i == n + 1:
            curs = ''.join([c for c in cur if c != ' '])
            return [cur] if eval(curs) == 0 else []
        result = brute(cur + f"+{i}", i + 1)
        result += brute(cur + f"-{i}", i + 1)
        result += brute(cur + f" {i}", i + 1)
        return result
    print('\n'.join(sorted(brute())) + '\n')