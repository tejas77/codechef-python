from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(map(int, stdin.readline().split()))
    ans.append(str((n-1) * min(nArr)))
stdout.write('\n'.join(ans))
