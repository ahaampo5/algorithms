# 21.07.22
# Z
#
import sys 
input = sys.stdin.readline

n, r, c = map(int, input().split())


answer = 0
stand = 2**(n-1)

while stand > 0:
    r_a, c_a = (r//stand, c//stand)
    if (r_a,c_a)==(0,0):
        pass
    elif (r_a, c_a) ==(0,1):
        answer += stand**2
        c -= stand
    elif (r_a, c_a) == (1,0):
        answer += 2*stand**2
        r -= stand
    else:
        answer += 3*stand**2
        c -= stand
        r -= stand
    
    stand //= 2

print(answer)
