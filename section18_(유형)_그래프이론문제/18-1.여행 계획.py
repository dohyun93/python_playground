import sys
input = sys.stdin.readline

def findRoot(parent, a):
    if parent[a] != a:
        parent[a] = findRoot(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    aRoot = findRoot(parent, a)
    bRoot = findRoot(parent, b)

    if aRoot < bRoot:
        parent[bRoot] = aRoot
    else:
        parent[aRoot] = bRoot

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for n in range(N):
        graph.append(list(map(int, input().split())))
    path = list(map(int, input().split()))

    parent = [i for i in range(N)]

    for r in range(N):
        for c in range(N):
            if graph[r][c] == 1:
                union(parent, r, c)

    commonRoot = parent[path[0]]
    answer = "YES"
    for p in path:
        curRoot = parent[p]
        if curRoot != commonRoot:
            answer = "NO"
            break

    print(answer)