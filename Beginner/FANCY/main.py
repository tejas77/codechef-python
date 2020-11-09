from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    s = stdin.readline().split()
    stdout.write('Real Fancy\n' if 'not' in s else 'regularly fancy\n')
