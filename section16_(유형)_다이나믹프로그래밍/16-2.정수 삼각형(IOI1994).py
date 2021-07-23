# 정수 삼각형
#    0
#   1 2
#  3 4 5
# 이런 것을 정수 삼각형 이라고 한다. 아래층의 수는 왼쪽 위 또는 오른쪽 위에서 선택 가능
# 삼각형 n (크기/높이)은 500이하 자연수이고 이 때 만들 수 있는 가장 큰 수는?

import sys

n = int(input())
triangle = []
for h in range(n):
    triangle.append(list(map(int, sys.stdin.readline().rsplit())))

for r in range(1, n):
    for c in range(r+1):
        if c == 0:
            upleft = 0
        else:
            upleft = triangle[r-1][c-1]

        if c == r:
            upright = 0
        else:
            upright = triangle[r-1][c]

        triangle[r][c] = triangle[r][c] + max(upleft, upright)

print(max(triangle[n-1]))