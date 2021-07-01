import sys
import heapq

input = sys.stdin.readline
n = int(input())

h = []
answer = []
for _ in range(n):
    a = int(input())
    if len(h) == 0 and a == 0:
        answer.append(0)
    elif a != 0:
        heapq.heappush(h, a)
    else:
        answer.append(heapq.heappop(h))
for i in answer:
    print(i)

