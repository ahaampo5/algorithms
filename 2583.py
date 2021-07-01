# 영역 구하기
# 21.06.30
#

import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())

cor = [[0]*m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1,x2):
        for y in range(y1, y2):
            cor[x][y] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = []
visited = set()
for i in range(n):
    for j in range(m):
        queue = deque()
        queue.append((i,j))
        cnt = 0
        while queue:
            x_, y_ = queue.popleft()
            if cor[x_][y_] != 0:
                continue
            cor[x_][y_] = -1
            cnt += 1
            for k in range(4):
                x_n = x_+dx[k]
                y_n = y_+dy[k]
                if 0<= x_n < n and 0<= y_n < m and cor[x_n][y_n] == 0:
                    queue.append((x_n, y_n))
        if cnt != 0:
            answer.append(cnt)

print(len(answer))
print(' '.join(map(str, sorted(answer))))
        

