def solution(arr):
    stk = []
    for a in arr:
        if(len(stk)>0 and stk[-1]==a):
            stk.pop()
        else:
            stk.append(a)
    return stk if stk else [-1]