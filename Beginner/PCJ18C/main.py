from sys import stdin, stdout
from math import gcd
ans = []

for _ in range(int(stdin.readline())):
    n, a, k = map(int, stdin.readline().split())
    num = (a*n*(n-1))+((k-1)*(((n-2)*360)-(2*a*n)))
    den = n * (n - 1)
    z = gcd(num, den)
    ans.append(f'{int(num/z)} {int(den/z)}')
stdout.write('\n'.join(ans))
