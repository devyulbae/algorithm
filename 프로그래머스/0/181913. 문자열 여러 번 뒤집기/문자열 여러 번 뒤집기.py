def solution(my_s, queries):
    my_s = list(my_s)
    for s,e in queries:
        my_s[s:e+1] =  my_s[s:e+1][::-1]
    return ''.join(my_s)