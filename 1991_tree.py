import sys
from collections import deque

input = sys.stdin.readline

seq_list = ['210','201','021']

n = int(input().rstrip())

d = dict()
for _ in range(n):
    string = input().rstrip().replace(' ', '')
    d[string[0]] = string

answer = ['' for _ in range(3)]
for i in range(3):
    check = []
    queue = deque()
    queue.append('A')
    seq = seq_list[i]
    while queue:
        alpha = queue.pop()
        if alpha in check:
            answer[i] += alpha
            continue
        for j in seq:
            value = d[alpha][int(j)]
            if value == '.':
                continue
            else:
                queue.append(value)
        check.append(alpha)
for ans in answer:
    print(ans)
            
    


