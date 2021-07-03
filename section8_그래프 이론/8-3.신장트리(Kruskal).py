# 신장트리 (spanning tree)
# 신장트리는 그래프에서 모든 노드를 포함하되, 사이클이 존재하지 않는 부분그래프.

# 최소한의 비용으로 모든 노드를 연결하는 그래프를 만드는 알고리즘 두 가지. - minimum spanning tree
# 1. 크루스칼 알고리즘 - O(ElogE) - 그리디.
#   1-1 간선 데이터를 비용에 따라 오름차순 정렬 (logE)
#   2-1 간선 하나씩 순회하며 사이클 발생x일 경우 MST에 추가. 발생일경우 포함x.
#   3-1 모든 간선에 대해 2-1 적용. (E)
# 따라서 시간복잡도 O(ElogE).

def findRootAndSetParent(parent, x):
    if parent[x] != x:
        parent[x] = findRootAndSetParent(parent, parent[x])
    return parent[x] # 루트.

def union(parent, a, b):
    aRoot = findRootAndSetParent(parent, a)
    bRoot = findRootAndSetParent(parent, b)

    # a가 속한 집합으로 b를 union해야 함.
    # b루트의 루트값(=b루트, parent[parent[b]] = parent[bRoot])을 a의 루트값으로 바꿔야한다!
    if aRoot < bRoot:
        parent[bRoot] = aRoot
    else:
        parent[aRoot] = bRoot

v, e = map(int, input().split())
root = [0] * (v + 1)

edges = [] # 모든 간선
result = 0 # 최종 비용

for i in range(1, v+1):
    root[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort() # 비용 순으로 정렬.

for edge in edges:
    cost, a, b = edge
    # 같은 집합에 속해있다(=루트노드가 같다)는 조건이 아니면 현재 그래프에 포함이 안되어있다는 것이고,
    # MST를 만들기 위해 추가가 필요하다는 의미
    # 루트노드가 같다면 사이클이 발생한 것. (무향 그래프 기준.)
    if findRootAndSetParent(root, a) != findRootAndSetParent(root, b):
        union(root, a, b)
        result += cost

print(f"크루스칼 알고리즘을 통한 MST 비용: {result}")
# [input]
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

#[output]
#159