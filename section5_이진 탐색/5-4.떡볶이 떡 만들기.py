import sys
N, M = map(int, input().split())
riceCakes = list(map(int, sys.stdin.readline().rsplit()))

# 0 ~ max(riceCakes) 지정.
# mid 계산.
# start <= end 일 때 까지 함.

answer = 0
start = 0
end = max(riceCakes)
while start <= end:
    curH = (start + end) // 2
    curSum = 0
    for x in riceCakes:
        if x > curH:
            curSum += (x - curH)

    if curSum < M:
        end = curH - 1
    else:
        answer = curH
        start = curH + 1
print(answer)