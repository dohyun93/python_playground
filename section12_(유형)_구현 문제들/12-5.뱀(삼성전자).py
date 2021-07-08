from collections import deque

N = int(input())
WALL = -1
EMPTY = 0
APPLE = 1
BODY = 2
# 외부 padding포함 N+2가 한변길이. 초기 뱀 위치는 [1, 1], 방향은 오른쪽
# 0은 빈자리, -1은 외벽, 1은 사과, 2는 뱀
graph = [[0]*(N+2) for _ in range(N+2)]
# 외벽은 -1처리
for r in range(N+2):
    for c in range(N+2):
        if r == 0 or c == 0 or r == N+1 or c == N+1:
            graph[r][c] = WALL

# 동, 남, 서, 북
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d = 0
graph[1][1] = BODY

snake = deque([[1, 1]])

# 사과 위치
# 사과 먹으면 appendleft만 해주고.
# 사과 없으면 appendleft 한 다음에 pop.
K = int(input())
for k in range(K):
    a_r, a_c = map(int, input().split())
    graph[a_r][a_c] = APPLE

# 방향 변환정보
dirList = deque()
L = int(input())
for l in range(L):
    time, change = input().split()
    dirList.append([int(time), change])

time = 1
while True:
    curR, curC = snake[0][0], snake[0][1]
    nR, nC = curR + dr[d], curC + dc[d]
    # 외벽 닿는 경우
    if graph[nR][nC] == WALL:
        break
    # 몸에 닿는 경우
    elif graph[nR][nC] == BODY:
        break
    # 사과 먹는 경우
    elif graph[nR][nC] == APPLE:
        snake.appendleft([nR, nC])
        graph[nR][nC] = 2
    # 빈 공간인 경우 이동 후 꼬리 -1.
    elif graph[nR][nC] == EMPTY:
        snake.appendleft([nR, nC])
        del_r, del_c = snake.pop()
        graph[del_r][del_c] = 0
        graph[nR][nC] = 2
    # 방향 처리
    if dirList:
        changeTiming, howtoChange = dirList[0][0], dirList[0][1]
        if changeTiming == time:
            if howtoChange == "D":
                d += 1
                if d == 4:
                    d = 0
            elif howtoChange == "L":
                d -= 1
                if d == -1:
                    d = 3
            dirList.popleft()
    time += 1

print(time)