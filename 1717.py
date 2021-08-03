# 집합의 표현
# 21.08.03
#

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

group = [set([i]) for i in range(n+1)]

def union(a,b):
    if group[a] == group[b]:
        return None
    group[aa] = group[aa]|group[bb]
    s[b] = aa
    group[bb] = None

def check_union(a,b):
    result = None
    aa, bb = s[a], s[b]
    if group[aa] == group[bb]:
        result = 'YES'
    else:
        result = 'NO'
    return result

for _ in range(m):
    check, a, b = map(int, input().split())
    if check == 0:
        union(a,b)
    else:
        print(check_union(a,b))
