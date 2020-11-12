from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    nArr = list(map(int, stdin.readline().split()))
    nArr.sort()
    nArr = nArr[k:n-k]
    l = n - (2 * k)
    ans.append(str(sum(nArr) / l))
stdout.write('\n'.join(ans))
