import sys

# 1. 기본정보 입력 및 그래프 초기화.
# Note that node : 1 ~ N.
N, M = map(int, sys.stdin.readline().rsplit())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]
for m in range(M):
    src, dst = map(int, sys.stdin.readline().rsplit())
    graph[src][dst] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# 2. 플로이드 워셜 알고리즘 (O(N^3))
for k in range(1, N+1):
    for src in range(1, N+1):
        for dst in range(1, N+1):
            graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

# 3. node 잡고, 이 노드로 가는 경로가 있는 것(graph[src][node] != 0)의 수 +
#    이 노드에서 도달가능 경로의 노드의수 (graph[node][dst]) 결과 (간선 수) 가 N-1이면 정답 +1.
answer = 0
for node1 in range(1, N+1):
    cnt = 0
    for node2 in range(1, N+1):
        if graph[node1][node2] != INF or graph[node2][node1] != INF:
           cnt += 1
    if cnt == N: # 자기자신으로가는건 0이기때문에 30라인에서 +1 처리됨. 결국 N개만큼 조건만족 간선이 있는경우 정답처리.
        answer += 1
print(answer)