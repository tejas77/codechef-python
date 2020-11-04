import numpy as np
from sys import stdin, stdout
ans = []
modulo = 1000000007
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = np.array(list(map(int, stdin.readline().split())))
    dec = np.flip(np.arange(n), 0)
    nArr = np.sort(nArr)
    e = nArr - dec
    profit = np.sum(e[e > 0])
    ans.append(str(profit % modulo))
stdout.write('\n'.join(ans))
