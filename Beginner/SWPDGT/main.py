from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    l = []
    a, b = stdin.readline().split()
    if(len(a) == 1 and len(b) == 1):
        ans.append(str(int(a) + int(b)))
        continue
    elif(len(a) == 1):
        l.append(int(a)+int(b))
        l.append(int(b[0])+int(a[0]+b[1]))
        l.append(int(b[1])+int(b[0]+a[0]))
    elif(len(b) == 1):
        l.append(int(a)+int(b))
        l.append(int(b[0]+a[1])+int(a[0]))
        l.append(int(a[0]+b[0])+int(a[1]))
    else:
        l.append(int(a)+int(b))
        l.append(int(a[0]+b[0])+int(a[1]+b[1]))
        l.append(int(a[0]+b[1])+int(b[0]+a[1]))
        l.append(int(b[0]+a[1])+int(a[0]+b[1]))
        l.append(int(b[1]+a[1])+int(b[0]+a[0]))
    ans.append(str(max(l)))
stdout.write('\n'.join(ans))
