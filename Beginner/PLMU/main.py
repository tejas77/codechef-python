from sys import stdin, stdout
from math import floor
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(stdin.readline().split())
    c0, c2 = nArr.count('0'), nArr.count('2')
    ans.append(str(floor(c0*(c0-1)/2) + floor(c2*(c2-1)/2)))
stdout.write('\n'.join(ans))
