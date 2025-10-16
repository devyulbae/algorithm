import sys
n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

def solution(words):
    words = list(set(words))
    words.sort(key=lambda x : (len(x), x))
    for word in words:
        print(word)

solution(words)