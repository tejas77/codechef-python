from sys import stdin, stdout
ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = [i for i in range(1, n+1)]
    ans.append('yes' if a != b and len(set(a)) == max(a) == n else 'no')
stdout.write('\n'.join(ans))
