import sys
N = int(input())
soldiers = list(map(int, sys.stdin.readline().rsplit()))

# 가장 긴 증가하는 부분수열 (LIS) 문제 풀기
# 0 <= j < i 에 대해서 DP[i] = max(DP[i], DP[j]+1) if array[j] < array[i]
# DP[i]: array[i]를 마지막 원소로 갖는 부분수열의 최대 길이

soldiers.reverse()

dp = [1] * N
for i in range(N):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))