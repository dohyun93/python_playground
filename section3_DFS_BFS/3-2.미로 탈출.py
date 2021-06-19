# N x M 크기 지도에서 1은 지나갈 수 있음. 0은 못감.
# 1,1 에서 N,M까지 가는 데 최소 거리로.
import sys
from collections import deque
N, M = map(int, input().split())
graph = []
for _ in range(N):
    # 지도정보가 떨어져 들어온다면?
    #data = list(map(int, sys.stdin.readline().rsplit()))
    #data = list(map(int, input().split()))

    # 지도정보가 붙여서 들어온다면?
    data = list(map(int, input()))
    graph.append(data)
#print(graph)

visit = [[False]*M for _ in range(N)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

visit[0][0] = True
dq = deque([(0, 0, 1)])
answer = -1
while dq:
    top_r, top_c, dist = dq.popleft()
    if top_r == N-1 and top_c == M-1:
        answer = dist
        break
    for k in range(4):
        nr = top_r + dr[k]
        nc = top_c + dc[k]
        if 0 <= nr < N and 0 <= nc < M:
            if graph[nr][nc] == 1:
                if visit[nr][nc] == False:
                    dq.append((nr, nc, dist+1))
                    visit[nr][nc] = True

print(answer)
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
#
# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1
#
# 10