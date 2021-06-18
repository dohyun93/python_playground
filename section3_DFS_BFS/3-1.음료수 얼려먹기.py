from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
visited = [[0]*m for _ in range(n)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    dq = deque([(r, c)])
    visited[r][c] = 1
    while dq:
        r, c = dq.popleft()
        visited[r][c] = 1 # 방문.
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
            bfs(i, j)

print(answer)