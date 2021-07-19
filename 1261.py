# 21.07.16

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(input().rstrip())

visited = set()
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(start):
    q = []
    answer_list = []
    heappush(q, start)
    while q:
        y, x, answer, visited = heappop(q)
        if (y,x) in visited:
            continue
        visited.add((y,x))
        if (y,x) == (m,n):
            answer_list.append(answer)
            continue
        for i in range(4):
            y_n = y+dy[i]
            x_n = x+dx[i]
            if 0<=y_n<n and 0<=x_n<m and (y_n,x_n) not in visited:
                if arr[y_n][x_n] == '1':
                    answer += 1
                heappush(q, (y_n,x_n,answer, visited))

    return max(answer_list)

print(bfs((0,0,0,set())))