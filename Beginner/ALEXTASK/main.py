def solve(N, A):
    def gcd(X, Y):
        if not Y:
            return X
        return gcd(Y, X % Y)
    ans = A[0]*A[1]//gcd(A[0], A[1])
    for i in range(N):
        for j in range(i+1, N):
            ans = min(ans, A[i]*A[j]//gcd(A[i], A[j]))
    return ans

t = int(input())
for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))
