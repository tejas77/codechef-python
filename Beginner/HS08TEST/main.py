w, b = map(float, input().split())
w = int(w)
if w % 5 == 0 and w < (b-0.5):
    print(f'{b-0.5-w:.2f}')
else:
    print(f'{b:.2f}')
