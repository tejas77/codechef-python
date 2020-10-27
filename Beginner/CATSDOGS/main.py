t = int(input())

for _ in range(t):
    c, d, l = map(int, input().split())
    if l % 4 != 0:
        print('no')
    else:
        if c <= d * 2:
            print('yes' if (d * 4) <= l and l <= 4 * (c + d) else 'no')
        else:
            print('yes' if (c - (d * 2)) * 4 + (d * 4) <= l and l <= 4 * (c + d) else 'no')
