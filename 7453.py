# 합이 0인 네 정수
# 21.07.05
#
import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
answer = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if lst[i][0] + lst[j][1] + lst[k][2] + lst[l][3] == 0:
                    answer += 1
print(answer)