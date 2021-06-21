N, M = map(int, input().split()) # 코인 종류수 N, 목표금액 M
coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)

def dynamic_coin():
    dp = [10001] * (M+1)
    dp[0] = 0

    for n in range(N):
        for k in range(coins[n], M+1):
            if dp[k - coins[n]] != 10001:
                dp[k] = min(dp[k], dp[k-coins[i]]+1)

    if dp[M] == 10001:
        return -1
    else:
        return dp[M]

print(dynamic_coin())