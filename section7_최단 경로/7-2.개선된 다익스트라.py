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

for _ in range(numEdge):
    src, dst, cost = map(int, input().split())
    graph[src].append((cost, dst))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        curCost, curVertex = heapq.heappop(q)
        # 현재 노드에 대한 최단거리(정답)와 현재노드 cost 비교
        if distance[curVertex] < curCost:
            continue
        # 현재노드와 인접한 다른 노드 확인
        for pair in graph[curVertex]:
            newCost = curCost + pair[0] # 현재 cost에 graph의 비용 추가.
            if newCost < distance[pair[1]]:
                distance[pair[1]] = newCost
                heapq.heappush(q, (newCost, pair[1]))

dijkstra(start)

for i in range(1, numVertex+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(f"거리는 {distance[i]}입니다.")