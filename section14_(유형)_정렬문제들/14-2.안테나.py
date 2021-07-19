import sys

N = int(input())
data = list(map(int, sys.stdin.readline().rsplit()))
answer = 0
data = sorted(data)

idx1, idx2 = N // 2 - 1, N // 2
sum1, sum2 = 0, 0
for i in range(idx1):
    sum1 += data[idx1]-data[i]
for i in range(idx1+1, len(data)):
    sum1 += data[i] - data[idx1]

for i in range(idx2):
    sum2 += data[idx2] - data[i]
for i in range(idx2 + 1, len(data)):
    sum2 += data[i] - data[idx2]

answer = idx1 if sum1 < sum2 else idx2
if sum1 == sum2:
    answer = idx1

print(data[answer])