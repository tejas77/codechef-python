from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    d = stdin.readline()
    ans.append('Yes' if d.count('1') == 1 or d.count('0') == 1 else 'No')
stdout.write('\n'.join(ans))
