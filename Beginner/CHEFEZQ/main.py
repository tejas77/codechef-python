t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    q = list(map(int, input().strip().split()))
    cnt = 0
    for i in range(n):
        cnt += q[i]
        if cnt < k:
            print(i + 1)
            break
        cnt -= k
    if cnt > k:
        cnt = (cnt // k) + 1
        print(cnt + n)
