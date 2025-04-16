def solution(my_string):
    # 65-90: A, 97-122: a
    my_list = [0]*52
    for s in list(my_string):
        if s.isupper():
            my_list[ord(s)-65] += 1
        else:
            my_list[ord(s)-71] += 1
    return my_list