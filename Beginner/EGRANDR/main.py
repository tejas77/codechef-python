from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(map(int, stdin.readline().split()))
    if 2 not in nArr and 5 in nArr and (sum(nArr) / n) >= 4:
        ans.append("Yes")
    else:
        ans.append("No")
stdout.write('\n'.join(ans))
