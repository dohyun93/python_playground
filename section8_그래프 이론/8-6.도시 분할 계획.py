# N개의 집과 M개의 간선이 존재하며, 각 간선마다 유지비가 있다.
# 모든 집들간 간선이 있는 MST를 만들되, 이를 두 개로 분리하여 최소의 유지비를 갖도록 분할하려면 어떻게 할까?
# -> 크루스칼 알고리즘으로 O(ElogE) 시간복잡도로 MST를 만들고, 가장 유지비가 큰 간선을 삭제하면
# 두 개의 집단으로 나누는 동시에 모든 간선의 유지비를 최소로 지출할 수 있다.

def findRoot(roots, a):
    if a != roots[a]:
        roots[a] = findRoot(roots, roots[a])
    return roots[a]

def union(roots, a, b):
    aRoot = findRoot(roots, a)
    bRoot = findRoot(roots, b)
    if aRoot < bRoot:
        roots[bRoot] = aRoot
    else:
        roots[aRoot] = bRoot

N, M = map(int, input().split())
graph = []
for m in range(M):
    node1, node2, cost = map(int, input().split())
    graph.append((cost, node1, node2))

graph.sort()

answer = 0
roots = [0] * (N+1)
maxCost = -1

for i in range(1, N+1):
    roots[i] = i

for edge in graph:
    cost, node1, node2 = edge
    if findRoot(roots, node1) != findRoot(roots, node2):
        # 다른 루트노드를 갖는 cycle이 아니라면, 하나의 미니멈 스패닝트리에 두 노드를 추가.
        union(roots, node1, node2)
        answer += cost
        if maxCost < cost:
            maxCost = cost

answer -= maxCost

print(answer)