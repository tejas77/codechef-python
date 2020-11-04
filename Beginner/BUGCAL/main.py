from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    sum1, c, k, sum2 = 0, 0, 0, 0
    while a > 0 or b > 0:
        sum1 = (a % 10) + (b % 10)
        c = pow(10, k)
        k += 1
        sum2 += (sum1 % 10) * c
        a = int(a / 10)
        b = int(b / 10)
    ans.append(str(sum2))
stdout.write('\n'.join(ans))
