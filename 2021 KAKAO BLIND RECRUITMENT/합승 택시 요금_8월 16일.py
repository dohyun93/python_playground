# https://programmers.co.kr/learn/courses/30/lessons/72413
# 다익스트라 알고리즘을 이용한 최단거리 문제 풀이.

from heapq import heappush, heappop
INF = int(1e9)

def dijkstra(graph, start):
    n = len(graph)
    distance = [INF] * (n+1)
    q = [(0, start)] # 비용, start지점
    distance[start] = 0
    while q:
        cumulCost, curPos = heappop(q)
        if cumulCost > distance[curPos]:
            continue
        else:
            for dst, fare in enumerate(graph[curPos]): ### 아래와 다름
                if cumulCost + fare < distance[dst]:
                    distance[dst] = cumulCost + fare
                    heappush(q, (distance[dst], dst))
    return distance

def solution(n, s, a, b, fares):
    answer = INF
    graph = [[INF] * (n+1) for _ in range(1+n)]
    for src, dst, cost in fares:
        graph[src][dst] = cost ### 아래와 다름
        graph[dst][src] = cost
    for start in range(1, n+1):
        distance = dijkstra(graph, start)
        answer = min(distance[s] + distance[a] + distance[b], answer)
    return answer
#
# import heapq
#
# INF = int(1e9)
#
# def dijkstra(graph, start):
#     pq = [(0, start)]
#     distance = [INF] * len(graph)
#     distance[start] = 0
#
#     while pq:
#         cost, point = heapq.heappop(pq)
#         if distance[point] < cost:
#             continue
#         for dst, fare in graph[point]:
#             fare += cost
#             if fare < distance[dst]:
#                 distance[dst] = fare
#                 heapq.heappush(pq, (fare, dst))
#     return distance
#
# def solution(n, s, a, b, fares):
#     graph = [[] for _ in range(n+1)]
#     answer = INF
#     for src, dst, fare in fares:
#         graph[src].append((dst, fare))
#         graph[dst].append((src, fare))
#     for k in range(1, n+1):
#         dist_k = dijkstra(graph, k)
#         answer = min(answer, dist_k[s] + dist_k[a] + dist_k[b])
#     return answer