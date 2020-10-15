t = int(input())
for _ in range(t):
    p = int(input())
    menu = 0
    order = 11
    while p != 0:
        if p >= 2 ** order:
            p = p - 2 ** order
            menu = menu + 1
        else:
            order = order - 1
    print(menu)
