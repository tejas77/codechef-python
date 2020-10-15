t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(f'{max(a, b)} {a + b}')
