import math

def lcm(a, b):
    # 최소공배수를 계산하는 함수
    return abs(a * b) // math.gcd(a, b)
        
# input times
n = int(input())

for _ in range(n):
    # input
    a, b = map(int, input().split(" "))

    # output
    result = lcm(a, b)
    print(result)