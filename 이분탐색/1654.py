# 랜선 자르기
# 21.06.29
# 조건문을 쓸 때 그 상황을 구체적으로 생각해봐야한다.

import sys

input = sys.stdin.readline

k, n = map(int, input().split())

lan = []
for _ in range(k):
    lan.append(int(input().rstrip()))

left = 1
right = max(lan)
answer = 0
while left <= right:
    s = 0
    mid = (left+right)//2
    for i in lan:
        s += i//mid
    if s >= n: # 후보군
        left = mid + 1
        if answer < mid: # answer보다 클때만 갱신
            answer = mid
    else:
        right = mid - 1
print(answer)
