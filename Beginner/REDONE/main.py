from sys import stdin, stdout
res = [0]*1000001
res[1] = 1
mod = 1000000007

for i in range(2, 1000001):
    res[i] = i + res[i-1] + (res[i-1]*i) % mod

for _ in range(int(stdin.readline())):
    stdout.write(f"{res[int(stdin.readline())] % mod}\n")
