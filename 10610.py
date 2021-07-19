# 30
# 21.07.02
#
import sys
input = sys.stdin.readline

n = input().rstrip()

n_list = sorted(list(map(int,list(n))),reverse=True)
if '0' not in n:
    print(-1)
else:
    if sum(n_list)%3 == 0:
        print(''.join(list(map(str,n_list))))
    else:
        print(-1)
