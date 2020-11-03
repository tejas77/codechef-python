from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    a, b, c, d = map(int, stdin.readline().split())
    if a == b:
        ans.append("YES")
        continue
    elif c == d:
        ans.append("NO")
        continue
    dt = abs(a - b)
    sd = abs(c - d)
    ans.append("YES" if dt % sd == 0 else "NO")
stdout.write('\n'.join(ans))
