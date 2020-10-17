t = int(input())
for _ in range(t):
    n = int(input().strip()) + 1
    a = list(map(int, input().strip().split(' ')))
    t = a[0] ** 2
    k = 1
    s = 2 * a[0]
    modulo = (10 ** 9) +7
    for i in range(1, n):
        k *= 2
        t = t * 2 + s * a[i]
        s += k * a[i]
        t, k, s = t % modulo, k % modulo, s % modulo
    print((t - k * (a[0] ** 2)) % modulo)
