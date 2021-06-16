# N x M 크기의 지도에서 움직인 칸수 계산하기
# 규칙은 현재 위치에서 현재 방향을 기준으로 왼쪽 방향 으로 갈 곳 정함:
import sys
# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
Map = []
for i in range(N):
    Map.append(list(map(int, input().split())))
visited = [[0]*M for _ in range(N)] # 방문여부 확인.

# 최초 서있는 곳.
answer = 1
visited[r][c] = 1
turnTime = 0

def turnLeft():
    # step 1.
    global d
    global turnTime
    d = d - 1
    if d < 0:
        d = 3
    turnTime += 1

while True:
    print(r, c, d, turnTime)
    turnLeft()

    nr = r + dr[d]
    nc = c + dc[d]
    if nr >= 0 and nr < N and nc >= 0 and nc < M:
        if Map[nr][nc] == 0:
            if visited[nr][nc] == 0:
                r = nr
                c = nc
                visited[r][c] = 1
                answer += 1
                turnTime = 0
                continue

    if turnTime == 4:
        # step 3.
        nr = r - dr[d]
        nc = c - dc[d]

        # 바다/외부가 아니라 갈 수 있다면.
        if Map[nr][nc] == 0:
            r = nr
            c = nc
            # 이 경우 모두 가본 육지일 것이라 더하지 않음.
        # 밖이거나 바다면
        else:
            break
        turnTime = 0
print(answer)