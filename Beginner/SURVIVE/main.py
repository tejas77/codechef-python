from sys import stdin, stdout
from math import ceil, floor
ans = []

for _ in range(int(stdin.readline())):
    n, k, days = map(int, stdin.readline().split())
    req = k * days
    cBD = days - floor(days / 7)
    cB = cBD * n
    ans.append(str(ceil(req / n)) if req <= cB else "-1")
stdout.write('\n'.join(ans))
