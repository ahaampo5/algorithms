# 21.07.23
# 리모컨
#
import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
arr = list(map(int, input().split()))

for i in range(m):
    for j in range(arr):
        minimum = 1e9
        num = None
        for k in range(10):
            