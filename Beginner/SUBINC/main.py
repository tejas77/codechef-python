from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(map(int, stdin.readline().split()))
    total = [1] * n
    for i in range(1,n):
        if nArr[i-1] <= nArr[i]:
            total[i] += total[i-1]
    ans.append(str(sum(total)))
stdout.write('\n'.join(ans))
