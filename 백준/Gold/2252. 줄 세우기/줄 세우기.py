import sys
from collections import deque 
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
degree = [0]*(n+1)
q = deque()
answer_list = []

for _ in range(m):
    idx, num = map(int, sys.stdin.readline().split())
    graph[idx].append(num)
    degree[num] += 1 # 지목받을때마다 +1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i) # 포인터 큐에 넣는다

while q:
    node = q.popleft()
    answer_list.append(node)

    for next in graph[node]: # 다음 순번들에 1을 뺀다
        degree[next] -= 1
        if degree[next] == 0: # 0이 되면
            q.append(next) # 포인터 큐에 넣는다.

print(*answer_list)