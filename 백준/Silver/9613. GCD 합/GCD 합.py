import math

# input times
n = int(input())

for _ in range(n):  # for n times
    # 변수 초기화
    sum = 0
    # input nums as iterable
    nums = list(map(int, input().split()))
    # num 개수
    idx = nums[0]
    # calc output
    for x in range(1,idx+1):  # 1번~idx까지
        for y in range(x+1, idx+1): # x~idx까지 (x와 서로 다른 수)
            sum = sum + math.gcd(nums[x],nums[y])
    # print output
    print(sum)