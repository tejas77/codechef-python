from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    nArr = map(int, stdin.readline().split())
    c = len(list(filter(lambda x: x % 2 == 0, nArr)))
    ans.append("YES" if (k != 0 and c >= k) or (k == 0 and c != n) else "NO")
stdout.write('\n'.join(ans))
