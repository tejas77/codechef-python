from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    if n < 4:
        ans.append('-1')
        continue
    nArr = list(map(int, stdin.readline().split()))
    stk = list(filter(lambda x: nArr.count(x) >= 2, set(nArr)))
    if len(stk) < 2 and nArr.count(stk[0]) < 4:
        ans.append('-1')
        continue
    stk.sort(reverse=True)
    ans.append(f'{stk[0]*stk[0]}' if nArr.count(stk[0]) > 3 else f'{stk[0]*stk[1]}')
stdout.write('\n'.join(ans))
