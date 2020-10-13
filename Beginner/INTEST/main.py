n, k = map(int, input().split())
divisible = 0
while n > 0:
    if int(input()) % k == 0:
        divisible = divisible + 1
    n = n - 1
print(divisible)
