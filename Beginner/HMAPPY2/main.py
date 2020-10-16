from math import gcd

def lcm(a, b):
   return a*b // gcd(a, b)

t = int(input())
for _ in range(t):
    n, a, b, k = map(int, input().split())
    x = n//a
    y = n//b
    z = n//lcm(a, b)
    print('Win' if (x + y - (2 * z)) >= k else 'Lose')
