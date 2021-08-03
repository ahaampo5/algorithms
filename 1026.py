# 21.07.19
# 보물

import sys
input = sys.stdin.readline

n = int(input().rstrip())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)
answer = 0
for i in range(n):
    answer += A[i]*B[i]

print(answer)