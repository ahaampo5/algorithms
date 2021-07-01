import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

tomato_list = []
box = [[[] for _ in range(n)] for _ in range(h)]

for i in range(h):
    for j in range(n):
        tomato_row = list(map(int, input().split()))
        box[i][j] += tomato_row
        for k in range(m):
            if box[i][j][k] == 1:
                tomato_list.append((i,j,k,0))

dx = [0,0,0,0,1,-1]
dy = [0,0,-1,1,0,0]
dz = [1,-1,0,0,0,0]
num = 0
for loc in tomato_list:
    queue = deque()
    queue.append(loc)
    while queue:
        z, y, x, day = queue.popleft()
        for i in range(6):
            dx_n = x+dx[i]
            dy_n = y+dy[i]
            dz_n = z+dz[i]
            if all([0<=dx_n<m, 0<=dy_n<n, 0<=dz_n<h]) and box[dz_n][dy_n][dx_n] == 0:
                queue.append((dz_n, dy_n, dx_n))
                box[dz_n][dy_n][dx_n] = box[z][y][x] + 1
            else:
                continue
    day += 1
answer_1d = []
maximum = 0
for a in box:
    for b in a:
        if 0 in b:
            print(-1)
            exit(0)
        else:
            if maximum < max(b):
                maximum = max(b)
print(maximum-1)


