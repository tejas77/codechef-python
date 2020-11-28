from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    chef_paid = stdin.readline()
    total_amount = n * 1000
    total_amount -= chef_paid.count('1') * 1000
    first_late = chef_paid.find('0')
    if first_late != -1:
        total_amount += (n - (first_late/2)) * 100
    ans.append(str(int(total_amount)))
stdout.write('\n'.join(ans))
