import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
s = []
queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    row = list(map(int, input().split()))
    s.append(row)
    for j in range(m):
        if s[i][j] == 1:
            queue.append([i, j])

def bfs():
    max_v = 0
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x and x < n and 0 <= y and y < m and s[x][y] == 0:
                s[x][y] = s[a][b] + 1
                queue.append([x, y])

bfs()
for i in s:
    for j in i:
        
# s = sum(s, [])
# if 0 in s:
#     print(-1)
# else:
#     print(max(s)-1)