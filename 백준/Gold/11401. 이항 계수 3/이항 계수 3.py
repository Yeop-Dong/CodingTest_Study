n, k = map(int, input().split())
p = 1_000_000_007
# n!(k!(n-k)!)^-1 mod p
# = n!(k!(n-k)!)^(p-2) mod p
fact = [1] * (n+1)
for i in range(2, n+1):
    fact[i] = fact[i - 1] * i % p
result = fact[n] * pow(fact[k] * fact[n-k], p-2, p) % p
print(result)
