from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = stdin.readline().strip()
    s = sum(map(int, n)) % 10
    stdout.write(f"{n+str((10-s)%10)}\n")
