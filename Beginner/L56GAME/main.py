from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nOdd = len(list(filter(lambda x: x % 2, map(int, stdin.readline().split()))))
    ans.append('2' if n != 1 and (nOdd % 2) else '1')
stdout.write('\n'.join(ans))
