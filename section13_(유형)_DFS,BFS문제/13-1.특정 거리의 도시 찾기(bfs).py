from collections import deque
import sys
N, M, K, X = map(int, input().split())
# N x N 도시
# M개의 간선
# 출발지 X와 거리가 K 만큼 거리인 도시들 출력.

graph = [[] for _ in range(N+1)]
for m in range(M):
    src, dest = map(int, sys.stdin.readline().rsplit())
    graph[src].append(dest)
INF = int(1e9)
distance = [INF] * (N+1)
distance[0], distance[X] = 0, 0

dq = deque([X])
while dq:
    top = dq.popleft()
    for adj in graph[top]:
        if distance[adj] == INF:
            # 방문 안했으면 현재거리 +1 처리.
            distance[adj] = distance[top] + 1
            dq.append(adj)
        else:
            # 방문 했으면
            distance[adj] = min(distance[adj], distance[top] + 1)
answer = []
for idx, dist in enumerate (distance):
    if dist == K:
        answer.append(idx)

if answer:
    for ans in answer:
        print(ans)
else:
    print(-1)