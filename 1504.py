# 특정한 최단 경로
# 21.07.05
# 
import sys
from heapq import heappop, heappush
from collections import defaultdict
input = sys.stdin.readline

n, e = map(int, input().split())
g = defaultdict(lambda x:[])
for _ in range(e):
    a,b,c = map(int,input().split())
    g[a].append((c,b))

queue = []
heappush(queue, (1,0))
while queue:
    loc, dis = heappop(queue)
    