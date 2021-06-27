# 어떤 나라에는 N개의 도시가 있다.
# 각 도시는 보내고자 하는 메시지가 있을 경우, 다른 도시로 전보를 보내서 또다른 도시로 메시지를 전송할 수 있다.
# X->Y로 보내려면 통로가 있어야 한다.

# C라는 도시에서 위급 상화이 발생해서 최대한 많은 도시에 메시지를 보내려고 한다.
# 메시지는 도시 C에서 출발해서 각 도시 사이에 설치된 통로를 거쳐 최대한 많이 퍼져나갈 것이다.
# 각 도시 번호, 통로 설치 정보가 주어졌을 때,

# 1. 도시 C에서 보낸 메시지를 받게되는 도시의 갯수는 몇개이며,->자기자신, INF 아닌 도시
# 2. 도시들이 모두 메시지를 받는데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 구현하라.->최단거리 중 가장 긴 것.

# <입력>
# 도시 갯수 N, 통로 개수 M, 출발지 C
# 이후 2~M+1 라인에 걸쳐(M) 간선정보 주어짐. src, dst, cost.

# <출력>
# 메시지를 받는 총 도시 갯수, 총 걸리는 시간

import heapq

INF = int(1e9)
N, M, C = map(int, input().split())
# 한 지점에서 최단거리 -> 다익스트라 알고리즘. (O(ElogV)) -> E : 200000, V : 30000 -> 80만. O(V^2)였으면 9억....
distance = [INF] * (N+1)
graph = [[] for _ in range(1+N)]

# 1. 지도 그리기.
for i in range(M):
    src, dst, cost = map(int, input().split())
    graph[src].append((cost, dst))

q = []
heapq.heappush(q, (0, C))
distance[C] = 0

while q:
    frontCost, frontVertex = heapq.heappop(q)
    if distance[frontVertex] < frontCost:
        continue
    for adj in graph[frontVertex]:
        adjCost = adj[0]
        adjVertex = adj[1]
        if frontCost + adjCost < distance[adjVertex]:
            distance[adjVertex] = frontCost + adjCost
            heapq.heappush(q, (distance[adjVertex], adjVertex))

answerOne = 0
answerTwo = 0

for i in range(1, N+1):
    if i != C and distance[i] != INF:
        answerOne+=1

for i in range(1, N+1):
    if distance[i] != INF:
        answerTwo = max(answerTwo, distance[i])

print(answerOne, answerTwo)