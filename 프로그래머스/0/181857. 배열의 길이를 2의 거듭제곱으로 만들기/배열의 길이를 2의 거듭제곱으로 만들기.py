def solution(arr):
    l = len(arr)
    while(bin(l).count('1') != 1):
        l += 1
    return arr + [0]*(l-len(arr))