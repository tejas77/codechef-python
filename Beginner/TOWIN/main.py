from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().strip().split()))
    a.sort(reverse=True)
    if n == 1:
        stdout.write('first\n')
    elif n == 2:
        stdout.write('draw\n' if a[0] == a[1] else 'first\n')
    else:
        f, s = a[0], a[1] + a[2]
        a = a[3:]
        f += sum(a[0::2])
        s += sum(a[1::2])
        stdout.write(('first' if f > s else 'second' if s > f else 'draw') + "\n")
