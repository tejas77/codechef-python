from sys import stdin, stdout
from math import sqrt

a = 2 * int(stdin.readline())
b = -int(stdin.readline())
c = int(stdin.readline())
rt = sqrt(b*b - (2 * a * c))
x1 = (b + rt) / a
x2 = (b - rt) / a
stdout.write(f'{x1}\n{x2}')
