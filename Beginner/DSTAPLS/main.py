from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    ans.append("NO" if (n//k) % k == 0 else "YES")
stdout.write('\n'.join(ans))
