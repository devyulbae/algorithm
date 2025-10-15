def solution(nums):
    nums.sort(key=lambda x:(x[0], x[1]))
    for a,b in nums:
        print(a, b)


n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
solution(arr)