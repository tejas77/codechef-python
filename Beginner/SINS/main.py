from sys import stdin, stdout
from math import gcd
ans = []

for _ in range(int(stdin.readline())):
    m, b = map(int, stdin.readline().split())
    ans.append(str(2 * gcd(m, b)))
stdout.write('\n'.join(ans))
