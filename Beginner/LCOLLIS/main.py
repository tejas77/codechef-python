from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    cols = m * [0]
    for _ in range(n):
        cols = [x + y for x, y in zip(cols, map(int, list(stdin.readline().strip())))]
    cols = sum([(a * (a - 1) / 2) for a in cols])
    ans.append(str(int(abs(cols))))
stdout.write('\n'.join(ans))
