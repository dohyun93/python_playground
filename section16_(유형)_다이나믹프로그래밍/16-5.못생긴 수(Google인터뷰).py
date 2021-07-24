# 못생긴 수는 오직 2, 3, 5만을 소인수로 갖는 수를 의미한다.
# 1은 못생긴 수라고 할 때 n번째 못생긴 수를 구하시오.

n = int(input())
idx2, idx3, idx5 = 0, 0, 0
next2, next3, next5 = 2, 3, 5

dp = [0] * n
dp[0] = 1

for idx in range(1, n):
    dp[idx] = min(next2, next3, next5)
    if dp[idx] == next2:
        print("idx, 조건1", idx)
        idx2 += 1
        next2 = dp[idx2] * 2
    if dp[idx] == next3:
        print("idx, 조건2", idx)
        idx3 += 1
        next3 = dp[idx3] * 3
    if dp[idx] == next5:
        print("idx, 조건3", idx)
        idx5 += 1
        next5 = dp[idx5] * 5


print(dp[n-1])