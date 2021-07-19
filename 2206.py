# 벽 부수고 이동하기
# 21.07.05
# bfs 일때 deque 바로 적용하자. 인덱스, 개수 구별 확실하게 하자.
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
g = []
for _ in range(n):
    g.append(input().rstrip())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(y,x):
    global visited
    queue = deque()
    queue.append((y,x,0,1))
    while queue:
        y, x, b, cnt = queue.popleft()
        if (y,x) == (n-1,m-1):
            return cnt
        if (y,x) in visited:
            continue
        visited.add((y,x))
        for k in range(4):
            y_n = y+dy[k]
            x_n = x+dx[k]
            if 0<=y_n<n and 0<=x_n<m and (y_n,x_n) not in visited:
                if g[y_n][x_n] == '0':
                    queue.append((y_n,x_n,b, cnt+1))
                elif g[y_n][x_n] == '1' and b == 0:
                    queue.append((y_n,x_n,1, cnt+1))
visited = set()
answer = bfs(0,0)
if answer == None:
    print(-1)
else:
    print(answer)
