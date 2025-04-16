def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])