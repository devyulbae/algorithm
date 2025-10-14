
import sys
n = int(sys.stdin.readline())

answer_cnt = 0

for _ in range(n):
    x = str(input())
    x_dict = list()
    is_groupword = True
    
    x_dict.append(x[0])
    for i in range(1, len(x)):
        # 첫 등장
        if x[i] not in x_dict:
            x_dict.append(x[i])
        # 재 등장
        elif x[i] in x_dict and x[i-1] != x[i]:
            is_groupword = False
        
    if is_groupword:
        answer_cnt += 1

print(answer_cnt)