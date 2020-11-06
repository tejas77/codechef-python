from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(map(int, stdin.readline().split()))
    count, total = 0, 0
    for i in range(n):
        if nArr[i] % 2 == 0:
            count += 1
        else:
            total += count
    ans.append(str(total))
stdout.write('\n'.join(ans))
