import sys

input = sys.stdin.readline

n = int(input())

switchs = list(map(int, input().split()))

students_num = int(input().rstrip())

for _ in range(students_num):
    gender, num = map(int, input().rstrip().split())
    if gender == 1:
        stand = len(switchs)//num
        for i in range(1, stand+1):
            idx = i*num - 1
            switchs[idx] = 0 if switchs[idx]==1 else 1
    elif gender == 2:
        idx = num-1
        up = idx
        down = idx
        switchs[idx] = 0 if switchs[idx]==1 else 1
        for j in range(len(switchs)):
            up = up + 1
            down = down -1
            if up < len(switchs) and down >= 0:
                if switchs[up] == switchs[down]:
                    switchs[up] = 0 if switchs[up]==1 else 1
                    switchs[down] = 0 if switchs[down] == 1 else 1
                else:
                    break
            else:
                break

st = len(switchs)//20
for k in range(st+1):
    ans = switchs[k*20:(k+1)*20]
    if ans:
        print(' '.join(list(map(str, ans))))
