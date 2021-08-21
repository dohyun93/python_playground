from collections import deque

INF = int(1e9)
# 동, 서, 남, 북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 수직: 동남(02)/동북(03)/서남(12)/서북(13)/북동(30)/북서(31)/남동(20)/남서(21)
# 평행: 동동(00)/서서(11)/남남(22)/북북(33)/동서(01)/서동(10)/북남(32)/남북(23)
def solution(board):

    sqr_move = [(0, 2), (0, 3), (1, 2), (1, 3), (3, 0), (3, 1), (2, 0), (2, 1)]
    hor_move = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (1, 0), (3, 2), (2, 3)]

    q = deque()
    # (r, c, dir, cost)
    q.append((0, 0, 0, 0)) # 동
    q.append((0, 0, 2, 0)) # 남
    n = len(board)
    memo = [[INF] * n for _ in range(n)]

    answer = INF
    while q:
        r, c, dir, cost = q.popleft()
        if r == n-1 and c == n-1:
            answer = min(answer, cost)
            continue

        for n_dir in range(4):
            nr = r + dr[n_dir]
            nc = c + dc[n_dir]

            if nr <= -1 or nr >= n or nc <= -1 or nc >= n:
                continue

            if board[nr][nc]:
                continue

            costCumul = cost + (100 if (dir, n_dir) in hor_move else 600)
            if memo[nr][nc] != -1 and memo[nr][nc] < costCumul:
                continue

            q.append((nr, nc, n_dir, costCumul))
            memo[nr][nc] = costCumul

    return answer

board =[[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
result = solution(board)
print(result)

# 정답은 나오는데 시간 초과됨. - DFS.
# import sys
# INF = int(1e9)
# sys.setrecursionlimit(INF)
# answer = INF
#
# # 동서남북
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
# # 목적지 : [len(board)-1 , len(board)-1]
# def dfs(r, c, board, check, path, cost):
#     global answer
#     if r == len(board)-1 and c == len(board)-1:
#         answer = min(answer, cost)
#         return
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         if 0 <= nr < len(board) and 0 <= nc < len(board):
#             if board[nr][nc] == 0:
#                 if check[nr][nc] == False:
#                     check[nr][nc] = True
#                     path.append((nr, nc))
#                     if len(path) <= 2: # 직각무조건없음.
#                         dfs(nr, nc, board, check, path, cost+100)
#                     elif len(path) >= 3:
#                         p1_r, p1_c = path[-3][0], path[-3][1]
#                         r_diff1, c_diff1 = abs(p1_r - r), abs(p1_c - c)
#                         r_diff2, c_diff2 = abs(nr-r), abs(nc-c)
#                         if r_diff1 * r_diff2 + c_diff1 * c_diff2 == 0: # 수직
#                             dfs(nr, nc, board, check, path, cost+600)
#                         else:
#                             dfs(nr, nc, board, check, path, cost+100)
#                     path.pop()
#                     check[nr][nc] = False
#
# def solution(board):
#     global answer
#     check = [[False] * len(board) for _ in range(len(board))]
#     check[0][0] = True
#     dfs(0, 0, board, check, [(0, 0)], 0)
#     return answer