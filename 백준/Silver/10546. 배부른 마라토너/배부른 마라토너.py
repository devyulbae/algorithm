from collections import defaultdict, Counter
def solution(participant, completion):
    part_count = Counter(participant)
    for c in completion:
        part_count[c] -= 1
        if part_count[c] == 0:
            del part_count[c]
    return list(part_count.keys())[0]


n = int(input())
a = []
for i in range(n):
    a.append(input())
b = []
for i in range(n-1):
    b.append(input())
print(solution(a, b))