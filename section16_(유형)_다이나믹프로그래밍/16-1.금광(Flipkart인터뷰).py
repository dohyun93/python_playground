# n x m 크기의 금광이 있습니다.
# 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
# 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 어느 행에서든 출발할 수 있습니다.
# 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다.
# 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 촐력하는 프로그램을 작성하세요.

# [입력]
# T - 테스트 케이스 수. 아래 입력들 반복
# n m
# n*m개의 원소들 (공백으로 구분)

# 3개 방향 이동 가능 (오위, 오, 오아)

# 처음에는 첫 번째 열의 어디서든 출발 가능하다.
# 오른쪽으로 이동하면서 가장 큰 누적 금 합을 메모이제이션을 활용해 업데이트 한다.

import sys

dr = [-1, 0, 1]
dc = [1, 1, 1]

def maxGold(goldmap):
    # DP를 이용해 최대 금 구하기.
    # 첫 열의 dp값은 goldmap과 동일.
    n, m = len(goldmap), len(goldmap[0])
    dp = [[0] * m for _ in range(n)]
    for r in range(n):
        dp[r][0] = goldmap[r][0]

    # 열이 가장 최외곽 for로 와야함에 주의.
    for c in range(m):
        for r in range(n):
            for dir in range(3):
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr < n and 0 <= nc < m:
                    dp[nr][nc] = max(dp[nr][nc], dp[r][c] + goldmap[nr][nc])
    # 아래 방법으로 2차원 리스트에서 최대 값 뽑을 수 있음. 최소는 min으로 해주면 됨.
    return max(map(max, dp))

if __name__ == "__main__":
    T = int(input())
    answers = []
    for t in range(T):
        n, m = map(int, input().split())
        data = list(map(int, sys.stdin.readline().rsplit()))

        goldmap = []
        for r in range(n):
            goldmap.append(data[r*m:(r+1)*m])
        answers.append(maxGold(goldmap))
    for answer in answers:
        print(answer)