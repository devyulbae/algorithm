import sys
N = int(sys.stdin.readline())

cnt = 0
max_num= 0
arr = []

for _ in range(N):
    inp = int(sys.stdin.readline())
    arr.append(inp)

for num in arr[::-1]:
    if num > max_num:
        max_num = num
        cnt += 1
print(cnt)