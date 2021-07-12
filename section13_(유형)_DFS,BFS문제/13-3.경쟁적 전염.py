# NxN 크기의 시험관이 있다. 시험관은 1x1 크기의 칸으로 나누어지며, 특정한 위치에는 바이러스가 존재할 수 있다. 모든 바이러스는 1번부터 K번까지의 바이러스 종류 중 하나에 속한다.
# 시험관에 존재하는 모든 바이러스는 1초마다 상, 하, 좌, 우의 방향으로 증식해 나간다. 단, 매 초마다 번호가 낮은 종류의 바이러스부터 먼저 증식한다. 또한 증식 과정에서 특정한 칸에 이미 어떠한 바이러스가 존재한다면, 그 곳에는 다른 바이러스가 들어갈 수 없다.
# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 후에 (X,Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오. 만약 S초가 지난 후에 해당 위치에 바이러스가 존재하지 않는다면, 0을 출력한다. 이 때 X와 Y는 각각 행과 열의 위치를 의미하며, 시험관의 가장 왼쪽 위에 해당하는 곳은 (1,1)에 해당한다.

from collections import deque
import sys

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

if __name__ == '__main__':
    N, K = map(int, input().split())
    graph = []
    for n in range(N):
        row = list(map(int, sys.stdin.readline().rsplit()))
        graph.append(row)
    S, X, Y = map(int, input().split())

    data = []
    for r in range(N):
        for c in range(N):
            if graph[r][c] != 0:
                data.append((graph[r][c], 0, r, c))

    data_list = sorted(data)
    dq = deque(data_list)
    while dq:
        virus, time, row, col = dq.popleft()
        if time == S:
            break
        for idx in range(len(dr)):
            nr = row + dr[idx]
            nc = col + dc[idx]
            if 0 <= nr < N and 0 <= nc < N:
                if graph[nr][nc] == 0:
                    graph[nr][nc] = virus
                    dq.append((graph[nr][nc], time+1, nr, nc))

    answer = graph[X-1][Y-1] if graph[X-1][Y-1] != 0 else 0
    print(answer)