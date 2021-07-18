from collections import deque

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
d_horizon = [[0, 0, 1, -1], [0, 0, -1, -1], [-1, 1, 0, 0], [1, 1, 0, 0]]
d_vertical = [[0, 0, -1, -1], [0, 0, -1, 1], [1, 1, 0, 0], [1, -1, 0, 0]]

def checkInBoard(a, b, c, d, n):
    if 0 <= a < n and 0 <= b < n and 0 <= c < n and 0 <= d < n:
        return True
    return False

def reachToEnd(r, c, n):
    if r == n-1 and c == n-1:
        return True
    return False

def solution(board):
    n = len(board)
    answer = 0
    visit = [[0, 0, 0, 1]]
    dq = deque()
    dq.append([0, 0, 0, 1, 0])
    gameEnd = False
    while dq:
        fr, fc, sr, sc, time = dq.popleft()
        # 1. 상하좌우 이동
        for i in range(len(dr)):
            nfr = fr + dr[i]
            nfc = fc + dc[i]
            nsr = sr + dr[i]
            nsc = sc + dc[i]
            if checkInBoard(nfr, nfc, nsr, nsc, n):
                if board[nfr][nfc] == 0 and board[nsr][nsc] == 0:
                    if reachToEnd(nfr, nfc, n) or reachToEnd(nsr, nsc, n):
                        gameEnd = True
                        answer = time+1
                        break
                    else:
                        if [nfr, nfc, nsr, nsc] not in visit:
                            dq.append([nfr, nfc, nsr, nsc, time+1])
                            visit.append([nfr, nfc, nsr, nsc])
        if gameEnd:
            break
        #. 2. 회전이동
        # 2-1. 가로 상태일 경우
        if abs(sc - fc) == 1:
            for i in range(len(d_horizon)):
                diagonal_r, diagonal_c = 0, 0
                if i == 0: # 왼쪽pivot, 시계회전
                    # 1. 회전반경에 벽 체크
                    diagonal_r, diagonal_c = fr + 1, fc + 1
                elif i == 1:  # 왼쪽pivot, 반시계회전
                    diagonal_r, diagonal_c = fr - 1, fc + 1
                elif i == 2:  # 오른쪽pivot, 시계회전
                    diagonal_r, diagonal_c = sr - 1, sc - 1
                else:  # 오른쪽pivot, 반시계회전
                    diagonal_r, diagonal_c = sr + 1, sc - 1
                if checkInBoard(fr, fc, diagonal_r, diagonal_c, n): # 회전반경이 판 내부이고,
                    if board[diagonal_r][diagonal_c] == 0: # 그곳이 벽이 아니라면 이동위치 처리
                        nfr = fr + d_horizon[i][0]
                        nfc = fc + d_horizon[i][1]
                        nsr = sr + d_horizon[i][2]
                        nsc = sc + d_horizon[i][3]
                        if checkInBoard(nfr, nfc, nsr, nsc, n):
                            if board[nfr][nfc] == 0 and board[nsr][nsc] == 0:
                                if reachToEnd(nfr, nfc, n) or reachToEnd(nsr, nsc, n):
                                    gameEnd = True
                                    answer = time + 1
                                    break
                                else:
                                    if i == 1 or i == 3:
                                        if [nsr, nsc, nfr, nfc] not in visit:
                                            dq.append([nsr, nsc, nfr, nfc, time+1])
                                            visit.append([nsr, nsc, nfr, nfc])
                                    else:
                                        if [nfr, nfc, nsr, nsc] not in visit:
                                            dq.append([nfr, nfc, nsr, nsc, time+1])
                                            visit.append([nfr, nfc, nsr, nsc])
        if gameEnd:
            break
        # 2-2. 세로 상태일 경우
        elif abs(sr - fr) == 1:
            for i in range(len(d_vertical)):
                diagonal_r, diagonal_c = 0, 0
                if i == 0: # 위 pivot, 시계회전
                    # 1. 회전반경에 벽 체크
                    diagonal_r, diagonal_c = fr + 1, fc - 1
                elif i == 1:  # 위 pivot, 반시계회전
                    diagonal_r, diagonal_c = fr + 1, fc + 1
                elif i == 2:  # 아래 pivot, 시계회전
                    diagonal_r, diagonal_c = sr - 1, sc + 1
                else:  # 아래 pivot, 반시계회전
                    diagonal_r, diagonal_c = sr - 1, sc - 1
                if checkInBoard(fr, fc, diagonal_r, diagonal_c, n): # 회전반경이 판 내부이고,
                    if board[diagonal_r][diagonal_c] == 0: # 그곳이 벽이 아니라면 이동위치 처리
                        nfr = fr + d_vertical[i][0]
                        nfc = fc + d_vertical[i][1]
                        nsr = sr + d_vertical[i][2]
                        nsc = sc + d_vertical[i][3]
                        if checkInBoard(nfr, nfc, nsr, nsc, n):
                            if board[nfr][nfc] == 0 and board[nsr][nsc] == 0:
                                if reachToEnd(nfr, nfc, n) or reachToEnd(nsr, nsc, n):
                                    gameEnd = True
                                    answer = time + 1
                                    break
                                else:
                                    if i == 0 or i == 2:
                                        if [nsr, nsc, nfr, nfc] not in visit:
                                            dq.append([nsr, nsc, nfr, nfc, time+1])
                                            visit.append([nsr, nsc, nfr, nfc])
                                    else:
                                        if [nfr, nfc, nsr, nsc] not in visit:
                                            dq.append([nfr, nfc, nsr, nsc, time+1])
                                            visit.append([nfr, nfc, nsr, nsc])
        if gameEnd:
            break
    return answer