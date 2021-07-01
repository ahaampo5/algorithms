# import sys
# from heapq import heappop, heappush
# input = sys.stdin.readline

# V, E = map(int, input().split())

# start = int(input().rstrip())

# graph = {k:[] for k in range(1, V+1)}
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     graph[u].append((v,w))

# inf = 1e9
# dp = [inf] * (V+1)
# dp[start] = 0
# queue = []
# heappush(queue, (0, start))
# while queue:
#     weight, ver = heappop(queue)
#     if dp[ver] < weight:
#         continue
#     for v, w in graph[ver]:
#         w_n = weight + w
#         if dp[v] > w_n:
#             dp[v] = w_n
#             heappush(queue, (w_n, v))
# for j in range(1, V+1):
#     if dp[j] == inf:
#         print('INF')
#     else:
#         print(dp[j])

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

V, E = map(int, input().split())

start = int(input().rstrip())

graph = {k:[] for k in range(E+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

inf = 1e9
dp = [inf] * (V+1)
dp[start] = 0
queue = []
heappush(queue, (0, start))
while queue:
    weight, ver = heappop(queue)
    for v, w in graph[ver]:
        w_n = weight + w
        if dp[v] > w_n:
            dp[v] = w_n
            heappush(queue, (w_n, v))
for j in range(V+1):
    if j == 0:
        continue
    if dp[j] == inf:
        print('INF')
    else:
        print(dp[j])

