# K번 회사를 거쳐 X번 회사로 가는 최단거리
# 전형적인 플로이드 워셜 알고리즘 문제.

# X 도달 못할경우 -1 출력.

INF = int(1e9)

# 노드, 간선 갯수
n, m = map(int, input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

# 1. 자기자신 거리 0으로 초기화.
for src in range(1, n+1):
    for dst in range(1, n+1):
        if src == dst:
            graph[src][dst] = 0

# 2. 각 간선에 대한 정보 입력, 초기화.
for _ in range(m):
    src, dst = map(int, input().split())
    # 문제 조건 상 연결시 cost는 1, 양방향 이동 가능.
    graph[src][dst] = 1
    graph[dst][src] = 1

# 3. 최종목적지 X와 거쳐갈 장소 K 입력
X, K = map(int, input().split())

# 4. 플로이드 워셜 알고리즘.
for k in range(1, n+1):
    for src in range(1, n+1):
        for dst in range(1, n+1):
            graph[src][dst] = min(graph[src][dst], graph[src][k] + graph[k][dst])

# 5. 수행된 결과 출력
distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print("-1")
else:
    print(distance)