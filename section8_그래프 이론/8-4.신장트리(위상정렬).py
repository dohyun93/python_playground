# 위상정렬
# "순서가 정해져 있는 일련의 작업을 차례대로 수행"해야 할 때 사용할 수 있는 알고리즘.
# 방향그래프의 모든 노드를 방향성에 거스르지 않도록 "순서"대로 나열하는 것.

# [알고리즘]
# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. while q:
#        v = q.pop
#        for e in edges:
#            remove edge from graph where e(v -> somenode)
# 만약 모든 노드를 방문하기 전에 큐가 빈다면 사이클이 존재한다.

# 시간복잡도: O(V + E)
# 차례대로 모든 노드를 확인하면서, 해당 노드에서 출발하는 간선들을 차례대로 제거.

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1) # 진입차수
graph = [[] for i in range(v+1)]

# 방향 그래프 간선정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1

# 위상정렬 알고리즘
def topology_sort():
    result = [] # 알고리즘 수행 결과
    q = deque()

    for i in range(1, 1+v):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = ' ')

topology_sort()