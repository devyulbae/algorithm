def solution(myString, pat):
    return int("".join('B' if pat[x]=='A' else 'A' for x in range(len(pat))) in myString)