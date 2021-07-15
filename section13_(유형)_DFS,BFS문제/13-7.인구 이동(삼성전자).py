from collections import deque
N, L, R = map(int, input().split())
answer = 0
graph = []
for n in range(N):
    graph.append(list(map(int, input().split())))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 1. 상하좌우 연합 가능확인
def canMove():
    global graph
    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if L <= abs(graph[nr][nc] - graph[r][c]) <= R:
                        return True

    return False

# 2. 연합 계산
def makeUnion():
    global graph
    union = [[] for _ in range(N*N)]
    unionIdx = 0
    check = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if not check[r][c]:
                union[unionIdx].append([r, c])
                check[r][c] = True
                dq = deque([[r, c]])
                while dq:
                    curR, curC = dq.popleft()
                    for j in range(4):
                        nr = curR + dr[j]
                        nc = curC + dc[j]
                        if 0 <= nr < N and 0 <= nc < N:
                            if not check[nr][nc] and L <= abs(graph[nr][nc] - graph[curR][curC]) <= R:
                                union[unionIdx].append([nr, nc])
                                check[nr][nc] = True
                                dq.append([nr, nc])
                if len(union[unionIdx]) == 1:
                    union[unionIdx].pop()
                else:
                    unionIdx += 1
    return union

# 3. 인구 이동
def Move(union):
    global graph
    for u in union:
        sum = 0
        leng = len(u)
        if u:
            for element in u:
                curR = element[0]
                curC = element[1]
                sum += graph[curR][curC]
            newPop = sum // leng
            for element in u:
                curR = element[0]
                curC = element[1]
                graph[curR][curC] = newPop
        else:
            break

while True:
    if canMove():
        union = makeUnion()
        Move(union)
        answer += 1
    else:
        break
print(answer)