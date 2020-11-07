from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    nArr = list(map(int, stdin.readline().split()))
    rem = sum(min(x % k, k - (x % k)) for x in nArr)
    ans.append(str(rem))
stdout.write('\n'.join(ans))
