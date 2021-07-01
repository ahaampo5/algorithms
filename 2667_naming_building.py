import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
m = []
for _ in range(n):
    m.append(list(map(int,list(input().strip()))))

building = []
start = (0, 0)
q = deque()

dx = [1,0,0,-1]
dy = [0,-1,1,0]

def bfs(x, y):
    result = 0
    q.append((x,y))
    while q:   
        a, b = q.popleft()
        m[a][b] = 0
        result += 1
        for k in range(4):
            if a + dx[k] < 0 or a + dx[k] >= n or b + dy[k] < 0 or b + dy[k] >= n or m[a + dx[k]][b + dy[k]] == 0:
                continue
            else: 
                q.append((a+dx[k], b+dy[k]))
                m[a+dx[k]][b+dy[k]] = 0
    return result

for i in range(n):
    for j in range(n):
        result = 0
        if m[i][j] == 1:
            result = bfs(i, j)
        else:
            continue
        if result != 0:
            building.append(result)

print(len(building))
for n in sorted(building):
    print(n)
        



    
        

