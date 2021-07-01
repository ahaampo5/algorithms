# 플로이드
# 21.06.29
#
import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())

graph = {k:[] for k in range(1, n+1)}
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

answer = []
for i in range(1, n+1):
    start = i
    queue = []
    dp = [1e9] * (n+1)
    dp[start] = 0
    heappush(queue, (0, start))

    while queue:
        cost, location = heappop(queue)
        if dp[location] < cost:
            continue
        for l, c in graph[location]:
            cost_n = cost + c
            if cost_n < dp[l]:
                dp[l] = cost_n
                heappush(queue, (cost_n, l))
    answer.append(dp)
for ans in answer:
    ans_str = ' '.join(map(str, ans[1:]))
    print(ans_str.replace('1000000000', '0'))
