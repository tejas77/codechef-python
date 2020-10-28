from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    cans = list(stdin.readline())
    chefans = list(stdin.readline())
    w = list(map(int, stdin.readline().split()))
    k = 0
    for i in range(n):
        k += (1 if cans[i] == chefans[i] else 0)
    if k == n:
        stdout.write(f"{w[n]}\n")
        continue
    else:
        mW = w[0]
        for i in range(k+1):
            if w[i] > mW:
                mW = w[i]
        stdout.write(f"{mW}\n")
