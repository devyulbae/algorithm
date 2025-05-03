def solution(arr):
    cnt = -1
    while True:
        arr_post = []
        cnt += 1
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i]%2==0:
                arr_post.append(arr[i]//2)
            elif arr[i] < 50 and arr[i]%2==1:
                arr_post.append(arr[i]*2 +1)
            else:
                arr_post.append(arr[i])
                
        if arr_post == arr:
            return cnt
        else:
            arr = arr_post
            