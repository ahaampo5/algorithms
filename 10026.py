# 적록색약
# 21.07.05
# visited continue 고려 꼼꼼하게 하자.
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
m = []
for _ in range(n):
    value = input().rstrip()
    m.append(value)

dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(y, x, mode='RGB'):
    global visited
    queue = deque()
    queue.append((y,x))
    while queue:
        y, x = queue.popleft()
        if (y,x) in visited:
            continue
        visited.add((y,x))
        for k in range(4):
            y_n = y+dy[k]
            x_n = x+dx[k]
            if mode == 'RGB':
                if 0<=x_n<n and 0<=y_n<n and (y_n,x_n) not in visited and m[y_n][x_n] == m[y][x]:
                    queue.append((y_n,x_n))
            else:
                if 0<=x_n<n and 0<=y_n<n and (y_n,x_n) not in visited:
                    if m[y][x] == 'R' or m[y][x] == 'G':
                        if m[y_n][x_n] == 'R' or m[y_n][x_n] == 'G':
                            queue.append((y_n,x_n))
                    else:
                        if m[y_n][x_n] == 'B':
                            queue.append((y_n,x_n)) 
    return 1
answer = []
visited = set()
num = 0
for i in range(n):
    for j in range(n):
        if (j,i) in visited:
            continue
        num += bfs(j,i,'RGB')
answer.append(num)

visited = set()
num = 0
for i in range(n):
    for j in range(n):
        if (j,i) in visited:
            continue
        num+=bfs(j,i,'GGB')
answer.append(num)
print(' '.join(list(map(str,answer))))
