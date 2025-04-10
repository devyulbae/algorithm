def solution(n, control):
    n_dict = {'w': 1, 's': -1, 'd': 10, 'a': -10}
    for i in range(len(control)):
        n += n_dict[control[i]]
    return n