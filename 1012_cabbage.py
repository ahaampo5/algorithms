import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())

def init(width, height):
    return [[0]*width for _ in range(height)]

def main():
    m, n, k = map(int, input().rstrip().split())

    box = init(m, n)
    
    l = []
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        box[b][a] = 1
        l.append((b,a))
    
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    worm = 0
    for (d, c) in l:
        queue = deque()
        queue.append((d,c))
        while queue:
            y, x = queue.popleft()
            if box[y][x] == 1:
                box[y][x] = -1
                worm += 1
                for i in range(4):
                    x_n = x+dx[i]
                    y_n = y+dy[i]  
                    if 0 <= x_n and x_n < m and 0<= y_n and y_n < n and box[y_n][x_n] == 1:
                        queue.append((y_n, x_n))
                        box[y_n][x_n] += 1
                    else:
                        continue
            elif box[y][x] == 2:
                box[y][x] = -1
                for i in range(4):
                    x_n = x+dx[i]
                    y_n = y+dy[i]  
                    if 0 <= x_n and x_n < m and 0 <= y_n and y_n < n and box[y_n][x_n] == 1:
                        queue.append((y_n, x_n))
                        box[y_n][x_n] += 1
                    else:
                        continue
            else:
                continue
    return worm

answer = []
for _ in range(t):
    worm = main()
    answer.append(worm)
for j in answer:
    print(j)

# 중복 조심해봐라.
