t = int(input())

for _ in range(t):
    n, minX, maxX = map(int, input().split())
    total = maxX - minX + 1
    x, y, spam = 0, 1, 0
    even, odd = None, None
    for _ in range(n):
        wi, bi = map(int, input().split())
        x = ((wi*x)+bi) % 2
        y = ((wi*y)+bi) % 2

    if (minX % 2 != 0 and maxX % 2 == 0) or (minX  % 2 == 0 and maxX % 2 != 0):
        even = total / 2
        odd = even
    elif (minX % 2 != 0 and maxX != 0):
        even = total / 2
        odd = even + 1
    else:
        even = total / 2 + 1
        odd = even - 1
    
    if x % 2 != 0:
        spam += int(even)
    if y % 2 != 0:
        spam += int(odd)
    print(f'{total-spam} {spam}')
