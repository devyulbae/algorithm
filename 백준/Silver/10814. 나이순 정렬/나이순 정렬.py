import sys
def solution(member):
    member.sort(key=lambda x: x[0])
    for age, name in member:
        print(age, name)

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a, b = input().split()
    a = int(a)
    arr.append([a, b])
    
solution(arr)