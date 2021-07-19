# 21.07.16
# 

import sys 
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

answer_list = []
for k in range(len(a)):
    num = 0
    b_idx = 0
    dp = [1]*len(a)
    for i in range(k,len(a)):
        start = a[i]
        
        for j in range(b_idx,len(b)):
            if start == b[j] and j > b_idx:
                b_idx = j
                num+=1
                break
            elif start == b[j] and j <= b_idx:
                
    answer_list.append(num)
print(answer_list)
print(max(answer_list))