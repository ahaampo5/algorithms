import sys

input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))

result = 0
maximum = [0]
check = None

for i in range(len(seq)-1): # 0,1,2
    if seq[i] >= 0:
        maximum.append(maximum[-1]+seq[i])
    else:
        if check == None:
            check = seq[i]
            continue
        else:
            if maximum[-1] + seq[i] > maximum[-1] + check - seq[i]: # 6, 10
                maximum.append(maximum[-1] + seq[i])
            else:
                maximum.append(maximum[-1] + check - seq[i])
                check = seq[i] # 4
print(max(maximum))
# 10 6 9 10 15 21 -14 12 33 32
# 10 (6, 10) 13 14 19 25 (-10, 21) 33 54 (53, 19)


