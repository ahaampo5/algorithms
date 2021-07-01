import sys
input = sys.stdin.readline

n = int(input().strip())
schedule = []
for _ in range(n):
    schedule.append(list(map(int,input().split())))

sort_schedule = sorted(schedule, key=lambda x:x[1])

answer = []
last = 0
for i in sort_schedule:
    if last <= i[0]:
        answer.append(i)
        last = i[1]
    else:
        continue
print(len(answer))


