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