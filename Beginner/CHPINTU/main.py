from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    f = list(map(int, stdin.readline().split()))
    p = list(map(int, stdin.readline().split()))
    costs = {}
    for i in range(n):
        if f[i] in costs:
            costs[f[i]] += p[i]
        else:
            costs[f[i]] = p[i]
    ans.append(str(min(costs.values())))
stdout.write('\n'.join(ans))
