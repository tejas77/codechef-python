from datetime import date
from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    dt = date(int(stdin.readline()), 1, 1)
    ans.append(dt.strftime("%A").lower())
stdout.write('\n'.join(ans))
