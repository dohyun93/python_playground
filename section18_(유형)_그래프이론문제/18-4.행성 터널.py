# 행성 터널 성공출처다국어
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초	128 MB	10383	3838	2680	35.610%
# 문제
# 때는 2040년, 이민혁은 우주에 자신만의 왕국을 만들었다. 왕국은 N개의 행성으로 이루어져 있다. 민혁이는 이 행성을 효율적으로 지배하기 위해서 행성을 연결하는 터널을 만들려고 한다.
#
# 행성은 3차원 좌표위의 한 점으로 생각하면 된다. 두 행성 A(xA, yA, zA)와 B(xB, yB, zB)를 터널로 연결할 때 드는 비용은 min(|xA-xB|, |yA-yB|, |zA-zB|)이다.
#
# 민혁이는 터널을 총 N-1개 건설해서 모든 행성이 서로 연결되게 하려고 한다. 이때, 모든 행성을 터널로 연결하는데 필요한 최소 비용을 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 행성의 개수 N이 주어진다. (1 ≤ N ≤ 100,000) 다음 N개 줄에는 각 행성의 x, y, z좌표가 주어진다. 좌표는 -109보다 크거나 같고, 109보다 작거나 같은 정수이다. 한 위치에 행성이 두 개 이상 있는 경우는 없다.
#
# 출력
# 첫째 줄에 모든 행성을 터널로 연결하는데 필요한 최소 비용을 출력한다.

import sys

def findRoot(root, a):
    if root[a] != a:
        root[a] = findRoot(root, root[a])
    return root[a]

def union(root, a, b):
    aR = findRoot(root, a)
    bR = findRoot(root, b)

    if aR < bR:
        root[bR] = aR
    else:
        root[aR] = bR

def kruskal(Edges, N):
    root = [r for r in range(N)]
    answer = 0
    for e in Edges:
        if findRoot(root, e[1]) != findRoot(root, e[2]):
            union(root, e[1], e[2])
            answer += e[0]
    return answer

input = sys.stdin.readline
INF = int(1e9)

if __name__ == "__main__":
    N = int(input())
    answer = INF
    x = []
    y = []
    z = []
    Edges = []
    for n in range(N):
        data = list(map(int, input().split()))
        x.append((data[0], n))
        y.append((data[1], n))
        z.append((data[2], n))

    x.sort()
    y.sort()
    z.sort()

    for idx in range(N-1):
        Edges.append((x[idx+1][0]-x[idx][0], x[idx][1], x[idx+1][1]))
        Edges.append((y[idx + 1][0] - y[idx][0], y[idx][1], y[idx + 1][1]))
        Edges.append((z[idx + 1][0] - z[idx][0], z[idx][1], z[idx + 1][1]))

    Edges.sort()

    answer = kruskal(Edges, N)
    print(answer)

# 예제 입력 1
# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19
#
# 예제 출력 1
# 4