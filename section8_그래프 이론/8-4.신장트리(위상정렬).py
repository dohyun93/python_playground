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

# 위상정렬 알고리즘 - 그래프 알고리즘에서 순서가 정해진 일련의 작업 수행에 대한 순서대로 정렬하는 것.
# [input]
# v e
# e줄에 걸쳐 간선정보 (방향 그래프)

# [output]
# 방문 순서

# 큐를 이용해서 푼다. 큐는 deque.

from collections import deque

v, e = map(int, input().split())
result = []
graph = [[] for _ in range(v+1)]
indegree = [0] * (v+1)
q = deque()

# 간선정보 입력
for _ in range(e):
    src, dst = map(int, input().split())
    graph[src].append(dst)
    indegree[dst] += 1

def topologySort():
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)
        for dst in graph[cur]:
            indegree[dst] -= 1
            if indegree[dst] == 0:
                q.append(dst)


    for i in result:
        print(i, end = ' ')

topologySort()