# https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3

from collections import deque


def solution(board, moves):
    n = len(board)
    moves = [m - 1 for m in moves]  # 열 idx로 변경.
    q = deque()
    answer = 0
    for col in moves:
        for row in range(n):
            if board[row][col] != 0:
                lastele = -1
                # q가 존재하면
                if q:
                    lastele = q.pop()
                    # 끝 요소가 같으면 다시 안넣고 정답추가
                    if board[row][col] == lastele:
                        answer += 2
                    # 끝 요소가 다르면 다시 넣어주고 보드내용 넣어주기.
                    else:
                        q.append(lastele)
                        q.append(board[row][col])
                # q 비어있으면 넣기.
                else:
                    q.append(board[row][col])
                # 꺼냄 처리
                board[row][col] = 0
                break # 다음 move로.

    return answer