from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    nArr = list(filter(lambda x: not x % m, map(int, stdin.readline().split())))
    ans.append(str(2 ** len(nArr) - 1))
stdout.write('\n'.join(ans))
