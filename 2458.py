# 키 순서
# 21.07.07
#
import sys
input = sys.stdin.readline

def upstream():
    pass

def downstream():
    pass

n, m = map(input().split())
for _ in range(m):
    a, b = map(int,input().split())

answer = 0
for i in range(n):
    iknow = 0
    iknow += upstream()
    iknow += downstream()
    if iknow == (n-1):
        answer += 1
print(answer)