from sys import stdin, stdout
from math import ceil
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    nArr = list(stdin.readline())
    present = nArr.count('P')
    attReq = ceil(0.75 * n)
    proxReq = attReq - present
    attendance, proxy = present / n, 0
    if attendance >= 0.75:
        stdout.write("0\n")
    else:
        for i in range(2,n-2):
            if nArr[i] == 'A' and (nArr[i - 1] == 'P' or nArr[i - 2] == 'P') and (nArr[i + 1] == 'P' or nArr[i + 2] == 'P'):
                present += 1
        stdout.write(f"{proxReq}\n" if present >= 0.75 * n else "-1\n")
