from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    a, b, n = map(int, stdin.readline().split())
    if n % 2 == 0:
        ans.append(str(int(max(a, b) / min(a, b))))
    else:
        ans.append(str(int(max(2 * a, b) / min(2 * a, b))))
stdout.write('\n'.join(ans))
