# 2*n 타일링 2
# 21.06.29

import sys
input = sys.stdin.readline

n = int(input().rstrip())

dp = [0,1,3] # 0, 1, 3, 5,(n-1)+(n-2)+2
for i in range(3, n+1):
    dp.append((dp[i-1] + 2*dp[i-2])%10007)

print(dp[n])