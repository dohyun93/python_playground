from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def bfs(r, c):
    dq = deque([(r, c)])
    while dq:
        r, c = dq.popleft()
        graph[r][c] = 1 # 방문.
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if graph[nr][nc] == 0:
                    dq.append((nr, nc))
                    graph[nr][nc] = 1

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer += 1
            bfs(i, j)
print(answer)