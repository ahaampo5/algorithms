# 21.07.19
# 벌집

import sys
input = sys.stdin.readline

n = int(input().rstrip())

num = 1
stand = 1
answer = 0
while num < n:
    num_n = num + 6*stand
    if num < n <= num_n:
        answer = stand
        break
    else:
        num = num_n
        stand += 1

print(answer+1)