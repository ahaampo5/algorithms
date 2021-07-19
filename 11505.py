# 구간 곱 구하기
# 21.07.07
# 
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
def update(b):
    global lst
    if b == 1:
        return
    if b%2 == 0:
        lst[b//2] = lst[b]*lst[b+1]
    else:
        lst[b//2] = lst[b]*lst[b-1]
    update(b//2)

def get(b, c):
    pass
# 1 23 4567

for j in range(10):
    if (2**j <n <=2**(j+1)):
        lst = [0] * (2**(j+2)+1)
        start = 2**(j+1)
print(len(lst))
for _ in range(n):
    lst.append(int(input().rstrip()))

for _ in range(m+k):
    a,b,c = map(int,input().split())
    if a == 1:
        lst[b] = c
        update(start+b-1)
    else:
        get(b,c)
