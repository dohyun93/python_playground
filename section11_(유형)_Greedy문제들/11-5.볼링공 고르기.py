# N개의 볼링공과 공의 최대 무게 M이 주어졌을 때,
# 각자 다른 번호(무게 아님)의 공을 고르되, 같은 무게의 공을 고르지 않을 조합의 수를 구하시오.
# 전체 C 2에서 동일 무게 C 2 들의 값을 빼면 된다.

from itertools import combinations

N, M = map(int, input().split())
Balls = list(map(int, input().split()))
maxBall = max(Balls)

# 등장 횟수
cnt = [0] * (maxBall + 1)
for i in Balls:
    cnt[i] += 1

# 두 개 뽑는 조합의 수
pickTwo = len(list((combinations(Balls, 2))))

# pickTwo에서 뺄 동일수 C_2 들을 구하는 연산.
for i in range(1, maxBall+1):
    if cnt[i] <= 1:
        continue
    repeatNum = len(list(combinations([i]*cnt[i], 2)))
    pickTwo -= repeatNum

print(pickTwo)