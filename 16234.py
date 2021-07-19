# 인구 이동
# 21.07.02
# Union find 
import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
n,l,r = map(int,input().split())

m = []
for _ in range(n):
    m.append(list(map(int, input().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    global m, box, check, visited
    queue = deque()
    queue.append((i,j))
    box = [[[]]*n for _ in range(n)]
    num = 1
    m1 = deepcopy(m)
    while queue:
        y, x = queue.popleft()
        if (i,j) in visited:
            continue
        visited.add((y,x))
        for k in range(4):
            y_n = y+dy[k]
            x_n = x+dx[k]
            if 0<=x_n<n and 0<=y_n<n and l<=abs(m[y_n][x_n] - m[y][x])<=r and (y_n,x_n) not in visited:
                queue.append((y_n,x_n))
                m[i][j] += m[y_n][x_n]
                box[i][j].append((y_n,x_n))
                num+=1
    a, b = i, j
    for a, b in box[i][j]:
        m[a][b] = m[i][j]//num
    m[i][j] = m[a][b]
    if m1 != m:
        check=True
    
answer = 0
check = True
while check:
    visited = set()
    answer += 1
    check=False
    for i in range(n):
        for j in range(n):
            if (i,j) in visited:
                continue
            bfs(i,j)

print(answer-1)
