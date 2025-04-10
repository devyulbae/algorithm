def solution(numLog):
    str_dict = {1: 'w', -1: 's', 10: 'd', -10: 'a'}
    answer = ""
    for i in range(len(numLog)-1):
        answer += str_dict[numLog[i+1] - numLog[i]]
    return answer