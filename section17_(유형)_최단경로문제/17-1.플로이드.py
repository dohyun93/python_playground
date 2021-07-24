# 플로이드 워셜 알고리즘.
# dp[n][m] = min(dp[n][m], dp[n][k] + dp[k][m])
# 백준 최단거리(플로이드 워셜 알고리즘) 핵심유형 - https://www.acmicpc.net/problem/11404
#
# 문제
# n(2 ≤ n ≤ 100)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 각 버스는 한 번 사용할 때 필요한 비용이 있다.
#
# 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.
#
# 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
#
# 출력
# n개의 줄을 출력해야 한다. i번째 줄에 출력하는 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다. 만약, i에서 j로 갈 수 없는 경우에는 그 자리에 0을 출력한다.

import sys

n = int(input())
edge = int(input())
INF = int(1e9)

# 1. 그래프 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]
# 2. 자기자신으로가는 것 0 처리.
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0
# 3. 간선 정보 입력 받고, 중복된 출발/목적지 정보에 대해 비용은 최소값으로 처리
for _ in range(edge):
    src, dst, cost = map(int, sys.stdin.readline().rsplit())
    # print(src, dst, cost)
    graph[src][dst] = min(graph[src][dst], cost)
# 4. 플로이드 워셜 알고리즘.
for k in range(1, n+1):
    for src in range(1, n+1):
        for dst in range(1, n+1):
            graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

# 4. 도달 못하는 경우 0으로 처리
for src in range(1, n+1):
    for dst in range(1, n+1):
        if graph[src][dst] == INF:
            graph[src][dst] = 0

# 5. 정답 출력.
for r in range(1, n+1):
    for c in range(1, n+1):
        print(graph[r][c], end=' ')
    print()

# [input]
# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4
#
# [output]
# 0 2 3 1 4
# 12 0 15 2 5
# 8 5 0 1 1
# 10 7 13 0 3
# 7 4 10 6 0