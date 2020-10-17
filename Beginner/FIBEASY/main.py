def fib_no(number):
    binary = bin(number)
    ans = binary[2:]
    return(len(ans)-1)

arr = [0, 1]
for i in range(59):
    arr.append((arr[-1]+arr[-2]) % 10)

t = int(input())
for i in range(t):
    inp = int(input())
    num = pow(2, fib_no(inp))
    index = (num-1) % 60
    print(arr[index])
