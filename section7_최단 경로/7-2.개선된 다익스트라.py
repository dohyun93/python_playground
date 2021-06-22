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
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드/간선
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        # 가장 최단거리가 짧은 노드 정보 꺼내기
        dist, curVertex = heapq.heappop(hq)
        # 현재 노드가 이미 처리가 된 것이라면
        if distance[curVertex] < dist:
            continue
        for i in graph[curVertex]:
            cost = dist + i[1]
            if cost < distance[i[1]]:
                distance[i[0]] = cost
                heapq.heappush(hq, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])