from sys import stdin, stdout
ans = []
for _ in range(int(stdin.readline())):
    top = stdin.readline().strip()
    low = stdin.readline().strip()
    o, m, t = top[0]+low[0], top[1]+low[1], top[2]+low[2]
    res = ('o' in o and 'b' in m and 'b' in t) or (
        'o' in m and 'b' in o and 'b' in t) or ('o' in t and 'b' in o and 'b' in m)
    ans.append('yes' if res else 'no')
stdout.write('\n'.join(ans))
