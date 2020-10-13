from functools import reduce
t = int(input())
for _ in range(t):
    print(reduce(lambda a, b: a*b, range(1, int(input()) + 1)))
