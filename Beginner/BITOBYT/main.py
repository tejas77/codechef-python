from sys import stdin, stdout
ans = []

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    h = n % 26
    d = n // 26
    if h == 0:
        ans.append(f'0 0 {2**(d-1)}')
    elif h <= 2:
        ans.append(f'{2**d} 0 0')
    elif h <= 10:
        ans.append(f'0 {2**d} 0')
    elif h <= 26:
        ans.append(f'0 0 {2**d}')
stdout.write('\n'.join(ans))
