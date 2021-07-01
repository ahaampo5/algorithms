# 신입사원
# 21.06.30
#
import sys
input = sys.stdin.readline

t = int(input().rstrip())


answer = []
for _ in range(t):
    cnt = 1
    n = int(input().rstrip())
    r = []
    for _ in range(n):
        a, b = map(int, input().split())
        r.append((a,b))
    
    r.sort()
    Max = r[0][1]

    for i in range(1, n):
        if Max > r[i][1]:
            cnt += 1
            Max = r[i][1]
    answer.append(cnt)

for j in answer:
    print(j)

    




