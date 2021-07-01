# 타임머신
# 21.06.29
#

import sys
from heapq import heappush, heappop
from copy import deepcopy
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [1e9] * (n+1)
graph = {k:[] for k in range(1, n+1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
print(graph)
queue = []
start = 1
heappush(queue, (0, start))
while queue:
    print(dp)
    print(queue)
    cost, location = heappop(queue)
    # visited.add(location)
    # visited_n = deepcopy(visited)
    if cost > dp[location]:
        continue
    for l, c in graph[location]:
        cost_n = cost + c
        if dp[n] > cost_n:
            dp[n] = cost_n
            heappush(queue, (cost_n, l))

for i in dp[2:]:
    if i == 1e9:
        print(-1)
    else:
        print(i)

