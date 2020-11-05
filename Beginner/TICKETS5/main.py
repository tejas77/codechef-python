from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    t = stdin.readline().strip()
    if t[0] == t[1]:
        ans.append("NO")
        continue
    fArr = list(filter(lambda x: x != "", t.split(t[0:2])))
    ans.append("YES" if len(fArr) == 0 or (
        len(fArr) == 1 and fArr[0] == t[0] or fArr[0] == t[1]) else "NO")
stdout.write('\n'.join(ans))
