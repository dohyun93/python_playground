# N가지 종류의 화폐가 있다.
# 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 한다.
# 각 화폐는 몇개라도 사용 가능하며, 사용한 화폐의 구성은 같지만 순서만 다른것은 동일한 경우로 간주한다.

N, M = map(int, input().split()) # 코인 종류수 N, 목표금액 M
# 이후 N줄에 걸쳐 화폐 가치가 주어진다. (각 화폐가치는 10000이하의 자연수)

coins = []
for i in range(N):
    coin = int(input())
    coins.append(coin)

def dynamic_coin():
    dp = [10001] * (M+1)
    dp[0] = 0

    for c in range(N):
        for curValue in range(coins[c], M+1):
            dp[curValue] = min(dp[curValue], dp[curValue-coins[c]]+1)

    if dp[M] == 10001:
        return -1
    else:
        return dp[M]

print(dynamic_coin())