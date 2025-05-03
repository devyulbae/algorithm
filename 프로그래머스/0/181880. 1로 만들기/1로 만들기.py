def solution(num_list):
    cnt = 0
    for num in num_list:
        while num != 1:
            cnt += 1
            num = num //2
    return cnt