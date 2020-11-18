from sys import stdin, stdout

n = int(stdin.readline())
a = list(set(map(int, stdin.readline().split())))
a.sort()
if(len(a) == 1):
    stdout.write('0')
else:
    stdout.write(f'{a[-2] % a[-1]}')
