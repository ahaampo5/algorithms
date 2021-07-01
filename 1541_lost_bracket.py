import sys 
import re

input = sys.stdin.readline

form = input().rstrip()

p = re.compile(r'[0-9]')
nums = []
num = ''
mode = 'plus'
for i in form:
    if p.match(i):
        num += i
        continue
    if mode == 'minus':
        nums.append(int(num))
        num = '-'
    elif i == '-' and mode == 'plus':
        nums.append(int(num))
        mode = 'minus'
        num = '-'
    elif i == '+' and mode == 'plus':
        nums.append(int(num))
        num = ''
    # elif i =='-' and mode == 'minus':
    #     nums.append(int(num))
    #     num = '-'
nums.append(int(num))
print(sum(nums))



    
    