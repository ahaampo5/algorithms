import sys
input = sys.stdin.readline

n, m = map(int, input().split())
miro = [[]*m for _ in range(n)]

for i in range(n):
    miro[i].append(input().rstrip())
    