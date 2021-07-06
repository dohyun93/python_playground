# 크기가 N x N인 도시가 있다. 도시는 1 x 1 크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈칸, 치킨집,
# 집 중 하나다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸,
# 왼쪽에서부터 c번째 칸을 의미한다. r, c는 1부터 시작한다.
#
# 이 도시에 사는 사람들은 치킨을 매우 좋아한다.
# 치킨거리는 집과 가장 가까운 치킨집 사이의 거리다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
#
# 0은 빈칸, 1은 집, 2는 치킨집이다.
# 도시에 있는 치킨집 중 최대 M개까지만 남기고 나머지는 폐점 한다.
# 어떻게 폐점할 것을 고르면 도시의 치킨거리가 최소가 될지 도시의 최소 치킨거리를 구하시오.

# 2 <= N <= 50
# 1 <= M <= 13

# 전체 48라인.
from itertools import combinations

INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

homes = []
chicken = []

for r in range(N):
    for c in range(N):
        if graph[r][c] == 1:
            homes.append((r, c))
        elif graph[r][c] == 2:
            chicken.append((r, c))

chickenIdx = [i for i in range(len(chicken))]

answer = INF
# 1개 ~ M개 고르고 그 때의 각 집의 치킨거리를 구한 뒤, 도시의 치킨거리 계산.
for picknum in range(1, M+1):
    if picknum == 1:
        oneChickenCityDist = INF
        for ch_idx in chickenIdx:
            curChickenMinDist = 0
            for home in homes:
                curChickenMinDist += abs(chicken[ch_idx][0]-home[0]) + abs(chicken[ch_idx][1]-home[1])
            # 도시 치킨 거리 갱신.
            oneChickenCityDist = min(oneChickenCityDist, curChickenMinDist)
        answer = min(answer, oneChickenCityDist)
        continue
    # 2개 이상 M개 이하 치킨집 고르는 경우
    Combinations = list(combinations(chickenIdx, picknum))

    for Combi in Combinations:
        curCombiCityDist = 0
        for home in homes: # (r, c)
            curHomeR, curHomeC = home
            minVal = INF
            for com in Combi: # 3
                curHomeMinDist = min(minVal, abs(chicken[com][0] - curHomeR) + abs(chicken[com][1] - curHomeC))
                if curHomeMinDist != INF:
                    minVal = curHomeMinDist
            curCombiCityDist += minVal
        answer = min(answer, curCombiCityDist)
print(answer)

# [INPUT]
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2
#
# [OUTPUT]
# 5
#
# [INPUT]
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2
#
# [OUTPUT]
# 10
#
# [INPUT]
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
#
# [OUTPUT]
# 11