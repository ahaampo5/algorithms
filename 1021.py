import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

goal = list(map(int, input().split()))

queue = deque(list(range(1, n+1))) # tuple도 바로가능?
answer = 0

def option2(queue):
    value = queue.popleft()
    queue.append(value)
    return queue

def option3(queue):
    value = queue.pop()
    queue.appendleft(value)
    return queue

for i in goal:
    idx = queue.index(i)
    if queue[0] == i:
        queue.popleft()
        continue
    if idx <= len(queue)-idx:
        for j in range(idx):
            option2(queue)
            answer += 1
    else:
        for j in range(len(queue)-idx):
            option3(queue)
            answer += 1
    queue.popleft()

print(answer)