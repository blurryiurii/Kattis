m, n, k = map(int, input().split())
pairs = []
for _ in range(n):
    pairs.append(list(map(int, input().split())))
dp = [0] * (m+1)
for i in range(n):
    a, b = pairs[i]
    for j in range(m + 1):
        if dp[j] == i:
            dp[(j+a)%m] = i + 1
            dp[(j+b)%m] = i + 1
print(dp[k])