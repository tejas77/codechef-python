t = int(input())

for _ in range(t):
    string = input()
    sorted_string = sorted(list(set(list(string))))
    if len(sorted_string) < 3:
        print('Dynamic')
    else:
        counts = []
        flag = 0
        for i in sorted_string:
            counts.append(string.count(i))
        counts.sort()
        n = len(counts)
        if counts[n-1] == counts[n-2] + counts[n-3]:
            flag = 1
        if flag == 1:
            print('Dynamic')
        else:
            print('Not')
