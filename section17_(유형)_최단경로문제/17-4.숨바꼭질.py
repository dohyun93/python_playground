# 1번에서 최단거리를 각 지점까지 모두 구한 뒤(distance)
# 가장 먼 거리의 지점에 숨는다.
# 숨을 번호, 1번부터 거리, 동일거리의 헛간 개수 출력.

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for m in range(M):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

distance = [INF] * (N+1)
distance[0], distance[1] = 0, 0

q = []
heapq.heappush(q, (0, 1)) # 현재누적거리, 현재지점

while q:
    cumCost, curPos = heapq.heappop(q)
    if distance[curPos] < cumCost:
        continue
    for adjVertex in graph[curPos]:
        cost = cumCost + 1
        if cost < distance[adjVertex]:
            distance[adjVertex] = cost
            heapq.heappush(q, (distance[adjVertex], adjVertex))

print(distance)

maxDist = max(distance)
answer1, answer2, answer3 = 0, 0, 0
for i in range(len(distance)):
    if distance[i] == maxDist:
        answer1 = i
        break
answer2 = maxDist
for j in distance:
    if j == maxDist:
        answer3 += 1

print(answer1, answer2, answer3)