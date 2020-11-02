from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(map(int, stdin.readline().split()))
    cn_5 = cn_10 = 0

    for m in nArr:
        if m == 5:
            cn_5 += 1
        elif m == 10:
            if cn_5 > 0:
                cn_5 -= 1
                cn_10 += 1
            else:
                ans.append("NO")
                break
        else:
            if cn_10 > 0:
                cn_10 -= 1
            elif cn_5 > 1:
                cn_5 -= 2
            else:
                ans.append("NO")
                break
    else:
        ans.append("YES")
stdout.write('\n'.join(ans))
