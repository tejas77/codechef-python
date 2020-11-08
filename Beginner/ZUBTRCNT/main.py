from sys import stdin, stdout
ans = []

for i in range(1, int(stdin.readline()) + 1):
    l, k = map(int, stdin.readline().split())
    if k <= l:
        n = l - k + 1
        res = (n * (n + 1)) // 2
    else:
        res = 0
    ans.append(f'Case {i}: {res}')
stdout.write('\n'.join(ans))
