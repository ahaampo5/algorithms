import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

queue = deque([(n,0)])
check = set()
while queue:
    value, time = queue.popleft()
    check.add(value)
    if value == k:
        print(time)
        break
    if value*2 not in check and value*2 < 2*k:
        queue.append((value*2, time+1))
    if value-1 not in check and value-1 > 0:
        queue.append((value-1, time+1))
    if value+1 not in check:
        queue.append((value+1, time+1))

