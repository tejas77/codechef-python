n, k = map(int, input().split())
modulo = (10 ** 9) + 7
arr = []

def fib(n, k):
    if n <= k:
        return 1
    else:
        t = k
        for i in range(n):
            if i < k:
                arr.append(1)
            else:
                arr.append(t)
                t += (arr[-1]-arr[i-k])
        return arr[-1] % modulo

print(fib(n, k))
