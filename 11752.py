import sys
from collections import deque
input  = sys.stdin.readline

n = int(input().rstrip())

mother = [0] * (n+1)
graph = {x:[] for x in range(1,n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
candidate = deque([1])
check = set()
while candidate:
    num = candidate.popleft()
    check.add(num)
    for j in graph[num]:
        if j not in check:
            mother[j] = num
            candidate.append(j)
for k in mother[2:]:
    print(k)
