from sys import stdin, stdout

ans = []
for _ in range(int(stdin.readline())):
    l, r = map(int, stdin.readline().split())
    count = (r - l) // 2
    if r & 1 or l & 1:
        count += 1
    ans.append('Odd' if count & 1 else 'Even')
stdout.write('\n'.join(ans))
