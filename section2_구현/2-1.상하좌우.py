# A는 N x N 정사각형 공간위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다.
# 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)이다. 상하좌우로 이동가능하며, 최초에는 (1,1)에 있다.
# L, R, U, D 순으로 좌우상하 로 방향을 제시받는다
# 입력>
# N
# 각 방향들
import sys
N = int(input())
Directions = list(sys.stdin.readline().rsplit())
curPos = [1, 1]

for dir in Directions:
    if dir == 'R':
        if curPos[1] + 1 <= N:
            curPos[1] += 1
        continue
    elif dir == 'L':
        if curPos[1] - 1 >= 1:
            curPos[1] -= 1
        continue
    elif dir == 'U':
        if curPos[0] - 1 >= 1:
            curPos[0] -= 1
        continue
    else:
        if curPos[0] + 1 <= N:
            curPos[0] += 1
        continue

print(curPos[0], curPos[1])