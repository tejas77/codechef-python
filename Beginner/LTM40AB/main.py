from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    a, b, c, d = map(int, stdin.readline().split())
    count = 0
    if a > b or c > d or a > d:
        ans.append(str(count))
        continue
    for i in range(a,b+1):
        if i < d:
            if i < c:
                count += d - c + 1
            else:
                count += d - i
    ans.append(str(count))
stdout.write('\n'.join(ans))
