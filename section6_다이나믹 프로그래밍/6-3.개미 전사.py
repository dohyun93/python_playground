# 개미전사
# 연속되어있는 형태의 창고의 음식을 먹을 때 인접한 창고를 동시에 털지 않고 먹을 수 있는 최대 음식 수는?

N = int(input())
food = list(map(int, input().split()))
dp = [0] * 100 # dp[i] : i 위치까지 최대 먹은 음식 수.
dp[0] = food[0]
dp[1] = max(dp[0], food[1])

if 0 <= N < 2:
    print(dp[N])
else:
    for i in range(2, N):
        dp[i] = max(food[i] + dp[i-2], dp[i-1])
        # 현재위치 먹고, -2위치의 최대 음식 수 VS 현재위치 안먹고 -1 위치의 최대 음식 수.

print(dp[N-1])