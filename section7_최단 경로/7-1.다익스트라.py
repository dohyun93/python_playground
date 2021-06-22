# 최단거리 노드 선형탐색 -> O(V^2)
# 알고리즘
# 1. 처음에 각 노드에 대한 최단거리를 담는 1차원 리스트를 선언한다.
# 2. 이후에 단계마다 방문하지 않은 노드 중에서 최단거리가 가장 짧은 노드를 선택하기 위해 매 단계마다 1차원 리스트의 모든 원소를 확인
#    (순차탐색) 한다.
# 아래 다익스트라는 특정 시작노드에서의 최단거리만을 다루지만, 전체 시작노드에 대해서는 별도 구현이 필요하다.

import sys
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def get_smallest_node():
    min_val = INF
    nearestIndex = 0
    for i in range(1, n+1):
        if distance[i] < min_val and not visited[i]:
            min_val = distance[i]
            nearestIndex = i
    return nearestIndex

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

# 총 O(V)번에 걸쳐서 최단거리가 가장 짧은 노드를 매번 선형탐색(O(V))해야 하므로, 총 시간복잡도는 O(V^2)이다.