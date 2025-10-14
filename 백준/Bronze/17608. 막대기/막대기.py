import sys

def solve():
    _ = input()
    S = tuple(map(int, sys.stdin))
    last = 0
    ans = 0
    for i in range(len(S)-1, -1, -1):
        if S[i] > last:
            last = S[i]
            ans += 1

    print(ans)


solve()