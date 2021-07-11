# 1~N까지의 도시와 M개의 단방향 간선이 존재한다.
# 거리는 1이고 X도시에서 출발해서 K거리만에 도착하는 모든 도시의 번호를 출력하는 프로그램을 개발하시오.
# 전형적인 다익스트라 알고리즘.

import heapq
INF = int(1e9)
N, M, K, X = map(int, input().split())
# 도시 N개, 도로 M개, 거리정보 K, 출발도시 X
graph = [[] for _ in range(N+1)]
for m in range(M):
    src, dst = map(int, input().split())
    graph[src].append((1, dst))

distance = [INF] * (N+1)
distance[X] = 0
hq = []
heapq.heappush(hq, (0, X))
while hq:
    top_cost, top_node = heapq.heappop(hq)
    if distance[top_node] < top_cost:
        continue
    for adj in graph[top_node]:
        adj_cost = adj[0]
        adj_node = adj[1]
        if top_cost + adj_cost < distance[adj_node]:
            distance[adj_node] = top_cost + adj_cost
            heapq.heappush(hq, (distance[adj_node], adj_node))

answer = [idx for idx, x in enumerate (distance) if x == K]
if answer:
    for i in range(len(answer)):
        print(answer[i])
else:
    print("-1")