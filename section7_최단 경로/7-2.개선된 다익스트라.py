# 개선된 다익스트라.
# O(ElogV)
# 힙 자료구조(heapq)를 이용한다.
#                   추출되는 데이터
# 스택         가장 나중에 삽입된 데이터
# 큐          가장 먼저 삽입된 데이터
# 힙          가장 우선순위가 높은 데이터

# 우선순위 큐 구현 방식
# 리스트 : 삽입 : O(1), 삭제 : O(N)
# 큐 :    삽입 : O(logN), 삭제 : O(logN) -> 완전 이진트리이므로 트리의 높이만큼 소요.

# 즉, 우리는 이전에 구현한 다익스트라에서 최단거리의 노드를 O(V)로 탐색하는 것 대신에,
# 우선순위 큐를 이용해 O(logV)으로 최단거리 노드를 탐색한다. -> 이를 E만큼 반복하므로 O(ElogV)가 된다.

import heapq
import sys
INF = int(1e9)
numVertex, numEdge = map(int, input().split())
start = int(input())
graph = [[] for _ in range(numVertex+1)]
distance = [INF] * (numVertex+1)

for edges in range(numEdge):
    src, dst, cost = map(int, input().split())
    graph[src].append((cost, dst))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cumulCost, curVertex = heapq.heappop(q)
        if distance[curVertex] < cumulCost:
            continue
        for adjCostAndVertex in graph[curVertex]:
            adjCost = adjCostAndVertex[0]
            adjVertex = adjCostAndVertex[1]
            if cumulCost + adjCost < distance[adjVertex]:
                distance[adjVertex] = cumulCost + adjCost
                heapq.heappush(q, (distance[adjVertex], adjVertex))

dijkstra(start)

for i in range(1, numVertex+1):
    if distance[i] != INF:
        print(f"{start}->{i}로의 최단 거리는 {distance[i]}이다.")
    else:
        print(f"{start}->{i}로는 도달할 수 없다.")