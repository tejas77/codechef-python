from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n = stdin.readline().strip()
    nSum = sum(list(map(int, list(n))))
    tenMinusSum = str(10 - ((nSum % 10) or 10))
    stdout.write(f"{n + tenMinusSum}\n")
