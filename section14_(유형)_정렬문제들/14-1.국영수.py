import sys
N = int(input())
scores = []
for i in range(N):
    data = list(map(str, sys.stdin.readline().rsplit()))
    for j in range(1, 4):
        data[j] = int(data[j])
    scores.append(data)

scores.sort(key=lambda x: [-x[1], x[2], -x[3], x[0]])
# 또는 위 6~7라인처럼 안해줬다면 scores.sort(key=lambda x: [-int(x[1]), int[2], -int(x[3]), x[0]]) 이렇게 해도됨.

for i in scores:
    print(i[0])