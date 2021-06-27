# 플로이드 워셜 알고리즘은 다익스트라 알고리즘과 달리 모든 지점에서 모든 지점까지의 최단거리를 구하는 알고리즘이다.
# 기존 dijkstra 알고리즘은 한 지점에서 다른 특정 지점까지의 최단 경로를 구하는 알고리즘 이다.

# Dijkstra : O(ElogV), 그리디 알고리즘
# 플로이드 워셜 : O(N^3), 다이나믹 프로그래밍 알고리즘

INF = int(1e9)
n = int(input()) # 노드 개수
m = int(input()) # 간선 개수
graph = [[INF] * (n+1) for _ in range(n+1)]

# 1. 자기 자신으로 가는 것 0으로 초기화.
for src in range(1, n+1):
    for dst in range(1, n+1):
        if src == dst:
            graph[src][dst] = 0

# 2. 각 간선에 대한 정보 입력.
for _ in range(m):
    src, dst, cost = map(int, input().split())
    graph[src][dst] = cost

# 3. 점화식에 따라 플로이드 워셜 알고리즘.
for midPoint in range (1, n+1):
    for src in range(1, n+1):
        for dst in range(1, n+1):
            graph[src][dst] = min(graph[src][dst], graph[src][midPoint] + graph[midPoint][dst])

# 4. 수행된 결과를 출력
for src in range(1, n+1):
    for dst in range(1, n+1):
        if graph[src][dst] == INF:
            print(f"{src}->{dst}는 도달 불가.")
        else:
            print(f"{src}->{dst} 최단거리는 {graph[src][dst]}")
    print()
