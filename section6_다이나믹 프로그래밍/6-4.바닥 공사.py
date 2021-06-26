# 1x2, 2x1, 2x2의 타일들이 주어졌을 때, 2 x N의 타일을 채우는 방법의 수를 796796으로 나눈 나머지 출력.
# dp[i]를 2 x i 타일을 채우는 경우의 수라고 할 때,
# dp[i]는 dp[i-1]에서 2x1 추가한 경우 -> dp[i-1] 해당
# 또한 dp[i-2]에서 2가지 (1x2 2개 또는 2x2 1개) 경우 -> dp[i-2]*2

N = int(input())
dp = [0] * 1001
DIV_NUM = 796796
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2] * 2) % DIV_NUM
    # -1위치까지 채우고 채우는 방법은 가로 1짜리 넣는 경우 1개. -> 즉 -1위치까지 최대 수 (dp[n-1])
    # 그리고 -2위치까지 채우고 채우는 방법은 2x2, 1x2 2개씩 채우는 방법이 있음. -> 즉, -2위치까지 최대 수 X 2 (dp[n-2] * 2)
print(dp[N])