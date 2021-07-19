# 포도주 시식
# 21.07.01
#
import sys
input = sys.stdin.readline

n = int(input())
lst = [0]
for _ in range(n):
    lst.append(int(input().rstrip()))

dp = [0] * (n+1)
for i in range(1,len(lst)):
    if i == 1 or i == 2:
        dp[i] = dp[i-1]+lst[i]
    else:
        dp[i] = max(dp[i-1], dp[i-3]+lst[i-1]+lst[i], dp[i-2] + lst[i])
print(max(dp))
