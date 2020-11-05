from sys import stdin, stdout
ans = []

a = int(stdin.readline())
b = int(stdin.readline())
c = stdin.readline()

ans.append(str(a + b if c == '+' else a - b if c ==
               '-' else a * b if c == '*' else a / b))
stdout.write('\n'.join(ans))
