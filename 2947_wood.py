import sys

input = sys.stdin.readline

wood = list(map(int, input().split()))

while 1:
    for i in range(4):
        if wood[i] > wood[i+1]:
            wood[i], wood[i+1] = wood[i+1], wood[i]
            print(' '.join(list(map(str, wood))))
    if wood != [1,2,3,4,5]:
        continue
    else:
        break