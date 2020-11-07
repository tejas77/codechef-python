from sys import stdin, stdout
from math import sqrt
ans = []

for _ in range(int(stdin.readline())):
    f, dTB, tA, bS = map(int, stdin.readline().split())
    bT = f / bS
    tT = sqrt(((f + dTB) * 2) / tA)
    ans.append('Tiger' if tT <= bT else 'Bolt')
stdout.write('\n'.join(ans))
