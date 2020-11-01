from sys import stdin, stdout
ans = []

def sequence(a, b):
    k = 0
    cur = b[k]
    for i in a:
        if i == cur:
            k += 1
            if k == len(b):
                return "Yes"
            cur = b[k]
    return "No"

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    seq = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())
    sSeq = list(map(int, stdin.readline().split()))
    if m > n:
        ans.append("No")
        continue
    ans.append(sequence(seq, sSeq))
stdout.write('\n'.join(ans))
