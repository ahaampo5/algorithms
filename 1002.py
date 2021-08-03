# 21.07.19
# 터렛
# 모든 경우의 수를 고려하자
import sys
import math
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if distance == 0:
        if r1==r2 and r1 != 0:
            print(-1)
        elif r1==r2 and r1 == 0:
            print(1)
        else:
            print(0)
    else:
        if distance > (r1+r2) or distance < abs(r1-r2):
            print(0)
        elif distance == (r1+r2) or distance == abs(r1-r2):
            print(1)
        else:
            print(2)
        