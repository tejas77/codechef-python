from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    a = set(stdin.readline().split())
    b = set(stdin.readline().split())
    ans.append(str(len(a.intersection(b))))
stdout.write('\n'.join(ans))
