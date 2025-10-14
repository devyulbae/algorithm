from collections import defaultdict

def solution(n, m, name):
        name_dict = defaultdict(int)
        answer = []
        for nm in name:
            if nm in name_dict:
                answer.append(nm)
            else:    
                name_dict[nm] = 1
        print(len(answer))
        for nm in sorted(answer):
            print(nm)
        
arr = []
n, m = map(int, input().split())
for i in range(n+m):
    arr.append(input())
solution(n, m, arr)