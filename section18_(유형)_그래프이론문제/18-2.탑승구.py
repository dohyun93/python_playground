import sys
input = sys.stdin.readline

def findRoot(root, a):
    if root[a] != a:
        root[a] = findRoot(root, root[a])
    return root[a]

def union(root, a, b):
    aRoot = findRoot(root, a)
    bRoot = findRoot(root, b)

    if aRoot < bRoot:
        root[bRoot] = aRoot
    else:
        root[aRoot] = bRoot

if __name__ == "__main__":
    G = int(input())
    P = int(input())

    # 일반 풀이
    # available = [] # 각 비행기가 도킹 가능한 정보들.
    # for p in range(P):
    #     available.append(int(input()))
    #
    # visited = [False] * (G+1)
    # answer = 0
    # for a in available:
    #     for airport in range(a, 0, -1):
    #         if not visited[airport]:
    #             visited[airport] = True
    #             answer += 1
    #             break
    # print(answer)

    # 서로소 집합 풀이
    # 현재 비행기가 n번 탑승구에 도킹 시, n-1과 n을 유니온 시킨다.
    # 즉, n번 도킹 시도시 연결이 되어있다면 그 이전 탑승구로 루트를 가리키게 되므로 해당 탑승구로 도킹 시도하게 한다.
    # 단 루트값이 0이면 이미 연결이 된 탑승구이므로 넘어간다.
    answer = 0
    root = [i for i in range(G+1)]
    for p in range(P):
        gi = int(input())
        # 아래처럼 -1씩해서 내려올 필요 없이, 바로 루트 찾아서 도킹 가능(루트 != 0)한지 파악 가능.
        # for node in range(gi, 0, -1):
        #     if root[node] != 0:
        #         answer += 1
        #         union(root, root[node], root[node]-1)
        #         break
        curRoot = findRoot(root, gi)
        if curRoot != 0:
            union(root, curRoot, curRoot-1)
            answer += 1

    print(answer)