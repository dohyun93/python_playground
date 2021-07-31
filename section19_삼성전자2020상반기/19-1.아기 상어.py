from collections import deque
import sys

INF = int(1e9)

n = int(input())
graph = []
cr, cc = 0, 0
csize = 2

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(len(graph[i])):
        if graph[i][j] == 9:
            cr, cc = i, j
            graph[cr][cc] = 0
            break

# 모든 위치까지 최단 거리만 계산
def bfs():
    dist = [[-1] * n for _ in range(n)]
    q = deque(  [(cr, cc)]  )
    dist[cr][cc] = 0

    while q:
        r, c = q.popleft()
        for j in range(4):
            nr, nc = r + dr[j], c + dc[j]
            if 0 <= nr < n and 0 <= nc < n:
                if dist[nr][nc] == -1 and graph[nr][nc] <= csize:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
    return dist

# 최단거리 테이블 주어졌을 때, 먹을 물고기 찾는 함수
def find(dist):
    r, c = 0, 0
    minDist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= graph[i][j] < csize:
                if dist[i][j] < minDist:
                    r, c = i, j
                    minDist = dist[i][j]
    if minDist == INF:
        return None
    else:
        return r, c, minDist

answer = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(answer)
        break
    else:
        cr, cc = value[0], value[1]
        answer += value[2]

        graph[cr][cc] = 0
        ate += 1

        if ate >= csize:
            csize += 1
            ate = 0