# https://programmers.co.kr/learn/courses/30/lessons/72413
# 다익스트라 알고리즘을 이용한 최단거리 문제 풀이.

import heapq

INF = int(1e9)

def dijkstra(graph, start):
    pq = [(0, start)]
    distance = [INF] * len(graph)
    distance[start] = 0

    while pq:
        cost, point = heapq.heappop(pq)
        if distance[point] < cost:
            continue
        for dst, fare in graph[point]:
            fare += cost
            if fare < distance[dst]:
                distance[dst] = fare
                heapq.heappush(pq, (fare, dst))
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    answer = INF
    for src, dst, fare in fares:
        graph[src].append((dst, fare))
        graph[dst].append((src, fare))
    for k in range(1, n+1):
        dist_k = dijkstra(graph, k)
        answer = min(answer, dist_k[s] + dist_k[a] + dist_k[b])
    return answer