# 21.07.16
# 
#
import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = list(map(int, input().split()))

dp = [1]*n
dp2 = [1]*n
for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

for i in range(len(lst)-2,-1,-1):
    for j in range(len(lst)-1,i,-1):
        if lst[i] > lst[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for k in range(len(dp)):
    dp[k] = dp[k] + dp2[k]

print(max(dp)-1)
