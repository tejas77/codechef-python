from sys import stdin, stdout
from math import sqrt
ans = []

for _ in range(int(stdin.readline())):
    n, h, y1, y2, l = map(int, stdin.readline().split())
    p, found = 0, False
    for i in range(n):
        typ, b = map(int, stdin.readline().split())
        if typ == 1 and h - y1 <= b:
            p += 1
        elif typ == 2 and y2 >= b:
            p += 1
        elif not found:
            l -= 1
            if l:
                p += 1
            elif not found:
                ans.append(str(p))
                for j in range(i+1,n):
                    stdin.readline()
                found = True
                break
    if not found:
        ans.append(str(p))
stdout.write('\n'.join(ans))
