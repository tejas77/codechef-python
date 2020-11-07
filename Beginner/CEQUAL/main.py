from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(stdin.readline().split())
    setN = set(nArr)
    ans.append("Yes" if len(nArr) != len(setN) else "No")
stdout.write('\n'.join(ans))