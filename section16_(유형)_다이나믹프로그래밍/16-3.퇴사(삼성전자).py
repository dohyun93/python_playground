import sys

N = int(input())
t, p = [], []
maxPay = 0

for n in range(N):
    data = list(map(int, sys.stdin.readline().rsplit()))
    t.append(data[0])
    p.append(data[1])

# 1. 완전탐색 (dfs) -> O(2^n)
def recur(day, pay, addedPay):
    if day > N:
        return pay-addedPay
    if day == N: # 딱 맞춰서 끝나는 경우.
        return pay
    work = recur(day+t[day], pay+p[day], p[day])
    notwork = recur(day+1, pay, 0)
    return max(work, notwork)

# maxPay = recur(0, 0, 0)

# 2. DP -> O(N^2)
def dp_solution():
    global maxPay
    # dp[N] : N일 일한거 포함 최대 금액.
    dp = [0] * N
    for day in range(N):
        if day + t[day] <= N:
            dp[day] = p[day]
            for j in range(day):
                if j + t[j] <= day:
                    dp[day] = max(dp[day], dp[j] + p[day])

    maxPay = max(dp)
    return maxPay

dp_solution()
print(maxPay)