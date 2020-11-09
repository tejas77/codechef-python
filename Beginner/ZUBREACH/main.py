from sys import stdin, stdout
ans = []

for i in range(1, int(stdin.readline()) + 1):
    m, n = map(int, stdin.readline().split())
    rx, ry = map(int, stdin.readline().split())
    s = int(stdin.readline())
    mov = stdin.readline()
    uc, dc, lc, rc = mov.count('U'), mov.count(
        'D'), mov.count('L'), mov.count('R')
    x, y = rc - lc, uc - dc
    if (x > m or y > n) or (x < 0 or y < 0):
        ans.append(f'Case {i}: DANGER')
    elif x == rx and y == ry:
        ans.append(f'Case {i}: REACHED')
    else:
        ans.append(f'Case {i}: SOMEWHERE')
stdout.write('\n'.join(ans))
