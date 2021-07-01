import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

schedule = [0]
for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t,p))
answer = 0
check = [0] * (n+1)
queue = deque([(0,0)]) # day, cost
while queue:
    day, cost = queue.popleft()
    if cost > answer:
        answer = cost
    if day+1 > n:
        continue
    day_pick = day+schedule[day+1][0]
    day_skip = day+1
    if day_pick <= n:
        queue.append((day_pick, cost+schedule[day+1][1]))
    if day_skip <= n:
        queue.append((day_skip, cost))

print(answer)




