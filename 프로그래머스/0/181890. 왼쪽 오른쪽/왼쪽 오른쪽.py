def solution(str_list):
    for idx, ch in enumerate(str_list):
        if ch == "l":
            return str_list[:idx]
        if ch == "r":
            if idx+1 == len(str_list):
                return []
            return str_list[idx+1:]
    return []