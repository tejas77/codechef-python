t = int(input())
for _ in range(t):
    n = int(input())
    rainbow = list(map(int, input().split()))
    j = n - 1
    c = 1
    flag = 1
    k = 0
    while k <= j:
        if rainbow[k] != rainbow[j] or rainbow[k] != c:
            flag = 0
            break
        if rainbow[k] < rainbow[k + 1] and c < 7:
            c += 1
        k += 1
        j -= 1
    print('no' if flag == 0 or c != 7 else 'yes')
