# 가장 큰 증가 부분 수열
# 21.07.01
#
import sys
input = sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))

d=[1]*n
d[0]=lst[0]
for i in range(1,n):
  for j in range(i):
    if lst[j]<lst[i]:
      d[i]=max(d[i], d[j]+lst[i])
    else:
      d[i]=max(d[i], lst[i])

print(max(d))
    