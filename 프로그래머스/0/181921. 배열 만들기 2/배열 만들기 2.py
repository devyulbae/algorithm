def solution(l, r):
    answer = []
    arr = [int(str(bin(i)[2:]).replace("1","5")) for i in range(64)]
    for i in arr:
        if i >= l and int(i) <= r:
            answer.append(i)
    
    return [-1] if len(answer)==0 else answer
    