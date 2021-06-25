from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[0]*m for _ in range(n)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def dfs(i, j):
    visited[i][j] = 1
    for k in range(4):
        nr = i + dr[k]
        nc = j + dc[k]
        if 0 <= nr < n and 0 <= nc < m:
            if graph[nr][nc] == 0:
                if visited[nr][nc] == 0:
                    dfs(nr, nc)

def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = 1
    while dq:
        r, c = dq.popleft() # 큐는 collections의 deque 사용. popleft, pop, append, appendleft
        visited[r][c] = 1 # 방문처리.
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 0:
                    if visited[nr][nc] == 0:
                        dq.append((nr, nc))

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            answer += 1
            #bfs(i, j)
            dfs(i, j)

print(answer)

# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111