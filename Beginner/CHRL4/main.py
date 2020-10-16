from math import log
n, k = map(int, input().split())
dp = [0] * n
ans = [0] * n
ki = 0
streets = list(map(int, input().split()))
for r in range(n):
    if k >= r:
        dp[r] = log(streets[r])
        ans[r] = streets[r]
    elif r - k - 1 == ki:
        e = dp[ki + 1:r]
        a = min(e)
        p = e.index(a)
        dp[r] = log(streets[r]) + a
        ki = ki + 1 + p
        ans[r] = (streets[r] * ans[ki]) % 1000000007
    else:
        dp[r] = log(streets[r]) + dp[ki]
        ans[r] = (streets[r] * ans[ki]) % 1000000007
print((streets[0] * ans[-1]) % 1000000007)
