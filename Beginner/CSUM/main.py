t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nArr = list(map(int, input().split()))
    temp = {nArr[0]}
    found = False
    for j in range(1,n):
        diff = k - nArr[j]
        if diff in temp:
            found = True
            break
        temp.add(nArr[j])
    print("Yes" if found else "No")
