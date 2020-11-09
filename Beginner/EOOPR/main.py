from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    x, y = map(int, stdin.readline().split())
    d = y - x
    if d == 0:
        ans.append('0')
    elif d > 0:
        if d % 2:
            ans.append('1')
        elif not d % 2 and d % 4:
            ans.append('2')
        else:
            ans.append('3')
    else:
        if d % 2:
            ans.append('2')
        else:
            ans.append('1')
stdout.write('\n'.join(ans))
