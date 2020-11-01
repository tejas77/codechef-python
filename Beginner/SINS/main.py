from sys import stdin, stdout
ans = []

def gcd(a, b):
    return b if a == 0 else gcd(b % a, a)

for _ in range(int(stdin.readline())):
    m, b = map(int, stdin.readline().split())
    ans.append(str(2 * gcd(m, b)))
stdout.write('\n'.join(ans))
