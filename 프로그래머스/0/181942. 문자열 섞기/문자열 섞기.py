def solution(str1, str2):
    return ''.join(str1[x]+str2[x] for x in range(len(str1)))