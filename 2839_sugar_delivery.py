import sys

input = sys.stdin.readline

n = int(input())

answer = 0

max_5 = n // 5

for i in range(max_5,-1, -1):
    remainder = n - i*5

    if remainder % 3 == 0:
        answer += i
        answer += (remainder // 3)
        break
    if i == 0 and (n % 3) != 0:
        answer = -1

print(answer)