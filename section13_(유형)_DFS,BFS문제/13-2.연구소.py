from itertools import combinations
from collections import deque
import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def makeMap():
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().rsplit()))
        graph.append(row)

    virus = []
    empty = []
    for r in range(N):
        for c in range(M):
            if graph[r][c] == 2:
                virus.append([r, c])
            elif graph[r][c] == 0:
                empty.append([r, c])

    return N, M, graph, virus, empty

    # bfs 로직
def findAnswer(N, M, graph_, dq):
    while dq:
        cR, cC = dq.popleft()
        for dir in range(4):
            nR = cR + dr[dir]
            nC = cC + dc[dir]
            if 0 <= nR < N and 0 <= nC < M:
                if graph_[nR][nC] == 0:
                    graph_[nR][nC] = 2
                    dq.append([nR, nC])
    cnt = 0
    for n in range(N):
        for m in range(M):
            if graph_[n][m] == 0:
                cnt += 1
    return cnt

if __name__ == "__main__":
    N, M, graph, virus, empty = makeMap()
    answer = -1
    for combi in list(combinations(empty, 3)):
        # graph_ = graph.copy()
        # graph_ = copy(graph)
        graph_ = [[0] * M for _ in range(N)]
        for r in range(N):
            for c in range(M):
                graph_[r][c] = graph[r][c]

        dq = deque(virus)
        # 현재 벽설치 조합에 대한 벽 처리
        for c in combi:
            graph_[c[0]][c[1]] = 1
        answer = max(answer, findAnswer(N, M, graph_, dq))

    print(answer)

# [INPUT 1]
# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
# [OUTPUT 1]
# 27
#
# [INPUT 2]
# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2
# [OUTPUT 2]
# 9
#
# [INPUT 3]
# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# [OUTPUT 3]
# 3