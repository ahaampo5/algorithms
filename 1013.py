# Contact
# 21.07.07
# regex
import sys
import re
input = sys.stdin.readline

p = re.compile(r'(100+1+|01)+')

n = int(input().rstrip())
for _ in range(n):
    string = input().rstrip()
    if p.fullmatch(string):
        print('YES')
    else:
        print('NO')