t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    mid = l//2
    a = []
    if n.count('9') == l:
        print('1' + '0' * (l-1) + '1')
    elif l % 2 == 0:
        a = n[:mid]
        a += a[::-1]
        if a > n:
            print(a)
        else:
            a = a[:mid]
            a = str(int(a) + 1)
            a += a[::-1]
            print(a)
    else:
        a = n[:mid+1]
        a += a[:-1][::-1]
        if a > n:
            print(a)
        else:
            a = a[0:mid+1]
            a = str(int(a) + 1)
            a += a[:-1][::-1]
            print(a)
