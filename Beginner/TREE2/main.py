from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    stdin.readline()
    nArr = set(stdin.readline().split())
    nArr.discard("0")
    ans.append(str(len(nArr)))
stdout.write('\n'.join(ans))
