# DP는 바텀업 방식으로 풀자.
# 이유는 탑다운으로 풀면 recursion depth 오류가 발생할 수 있다.

# 정수 X가 주어질 때, 아래 연산들을 활용해 1로만드는데 걸리는 최소 연산 수는?
# -1, 2로 나눠질 때 2로 나누기, 3, 5로 동일 하게 나누기.



X = int(input())
dp = [0] * 30001
for idx in range(2, X+1):
    dp[idx] = dp[idx-1]+1
    if idx % 2 == 0:
        dp[idx] = min(dp[idx//2]+1, dp[idx])
    elif idx % 3 == 0:
        dp[idx] = min(dp[idx//3]+1, dp[idx])
    elif idx % 5 == 0:
        dp[idx] = min(dp[idx//5]+1, dp[idx])
        # 5로 나눈것 vs 현재
print(dp[X])



# X = int(input())
# memo = [0] * 30001
# def makeOne(X):
#     for num in range(2, X+1):
#         memo[num] = memo[num-1] + 1
#         if num % 2 == 0:
#             memo[num] = min(memo[num//2]+1, memo[num])
#         elif num % 3 == 0:
#             memo[num] = min(memo[num // 3] + 1, memo[num])
#         elif num % 5 == 0:
#             memo[num] = min(memo[num // 5] + 1, memo[num])
#     return memo[X]
#
# print(makeOne(X))