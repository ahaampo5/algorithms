# 펠린드롬?
# 21.07.07
#
import sys
input = sys.stdin.readline

n = int(input().rstrip())
seq = list(map(int,input().split()))

m = int(input().rstrip())
for _ in range(m):
    s,e = map(int, input().split())
    piece = seq[s-1:e]    
    if piece == list(reversed(piece)):
        print(1)
    else:
        print(0)
