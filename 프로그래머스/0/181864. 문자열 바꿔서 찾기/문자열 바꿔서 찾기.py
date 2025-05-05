def solution(myString, pat):
    return int("".join('B' if x=='A' else 'A' for x in pat) in myString)