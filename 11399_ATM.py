import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

sort_m = sorted(m)
total = 0
for i in range(len(sort_m)):
    total += sum(sort_m[:(i+1)])

print(total)
