t = int(input())

for _ in range(t):
    n, k, x, y = map(int, input().split())
    aCs = [x]
    for _ in range(n):
        aC = (k + x) % n
        x = aC
        if aC in aCs:
            break
        aCs.append(aC)
    print('YES' if y in aCs else 'NO')
