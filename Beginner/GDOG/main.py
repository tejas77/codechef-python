from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    ans.append(str(max([n % x for x in range(1, k + 1)])))
stdout.write('\n'.join(ans))
