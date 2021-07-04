N = int(input())
fear = list(map(int, input().split()))
answer = 0
cnt = 0

for curfear in fear:
    cnt += 1
    if cnt >= curfear:
        cnt = 0
        answer += 1

print(answer)