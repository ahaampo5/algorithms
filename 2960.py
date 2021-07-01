# 에라토스테네스의 체
import sys

input = sys.stdin.readline

n, k = map(int,input().split())

inf = 1e9
answer_list = []
int_list = list(range(n+1))
int_list[0] = 1e9
int_list[1] = 1e9
while len(answer_list) != (n-1):
    stand = min(int_list)
    for i in int_list:
        idx = int_list.index(i)
        if idx % stand == 0 and i != inf:
            answer_list.append(i)
            int_list[idx] = inf

print(answer_list[k-1])