t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print('=' if a == b else '>' if a > b else '<')
