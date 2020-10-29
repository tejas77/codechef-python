from sys import stdin, stdout
l = [0, "sunday", "monday", "tuesday",
     "wednesday", "thursday", "friday", "saturday"]
ans = []
for _ in range(int(stdin.readline())):
    start, end, date1, date2 = stdin.readline().split()
    date1, date2 = int(date1), int(date2)
    d1, d2 = l.index(start), l.index(end)
    a = None
    a = (7 - d1 + d2) if d1 > d2 else(d2 - d1) if d1 < d2 else 0
    l1 = []
    while a + 1 <= date2:
        if date1 <= 1 + a and 1 + a <= date2:
            l1.append(1 + a)
        a += 7
    ans.append('impossible' if len(l1) == 0 else str(
        l1[0]) if len(l1) == 1 else 'many')
stdout.write('\n'.join(ans))
