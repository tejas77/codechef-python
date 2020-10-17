import math as m
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    lst1 = lst[:k]
    n = lst.count(max(lst1))
    r = lst1.count(max(lst1))
    print(int(m.factorial(n) / (m.factorial(n - r) * m.factorial(r))))
