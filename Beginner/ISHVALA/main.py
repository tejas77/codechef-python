from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    p, q = list(map(int, stdin.readline().split()))
    b, c, d = list(map(int, stdin.readline().split()))
    counta = 0
    countb = 0
    if b > 0:
        h = [int(i) for i in stdin.readline().split()]
        h.insert(0, 0)
        h.append(p+1)
        diffh = [h[i+1]-h[i]-1 for i in range(len(h)-1)]
        diffh = [i//d if i//d > 0 else 0 for i in diffh]
    else:
        diffh = [p//d]
    if c > 0:
        v = [int(i) for i in stdin.readline().split()]
        v.insert(0, 0)
        v.append(q+1)
        diffv = [v[i+1]-v[i]-1 for i in range(len(v)-1)]
        diffv = [i//d if i//d > 0 else 0 for i in diffv]
    else:
        diffv = [q//d]
    for i in diffh:
        counta += i
    for i in diffv:
        countb += i
    ans.append(str(counta * countb))
stdout.write('\n'.join(ans))
