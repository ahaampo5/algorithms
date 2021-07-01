import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

zombie = set()
queue = deque()
queue.append(1)
while queue:
    x = queue.pop()
    zombie.add(x)
    for i in graph[x]:
        if i not in zombie:
            queue.append(i)
print(len(zombie) - 1)
    
