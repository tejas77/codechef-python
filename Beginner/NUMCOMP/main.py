from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    a, b, n = map(int, stdin.readline().split())
    if a < 0 and n % 2 == 0:
        a = - a
    if b < 0 and n % 2 == 0:
        b = - b
    ans.append("1" if a > b else "2" if a < b else "0")
stdout.write('\n'.join(ans))
