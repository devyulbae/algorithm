def solution(arr, query):
    for i, q in enumerate(query):
        # 짝수
        if i%2==0:
            arr = arr[:q+1]   
        # 홀수
        else:
            arr = arr[q:]
    return arr