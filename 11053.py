# 가장 긴 증가하는 부분 수열
# 21. 07. 01
# 한번에 할려는 성향 때문에 접근을 이상하게 한다. n보고 시간복잡도 계산먼저.
import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))

d=[0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if lst[j]<lst[i] and d[i]<d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))