 # 당신은 화성 탐사 기계를 개발하는 프로그래머이다. 그런데 화성은 에너지 공급원을 찾기가 힘들다. 그래서 에너지를 효율적으로 사용하고자
 # 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동할 때 항상 최적의 경로를 찾도록 개발해야 한다.
 # 화성탐사 기계가 존재하는 공간은 N x N 크기의 2차원 공간이며, 각 칸을 지나가기 위한 비용이 존재한다. [0][0]에서 [n-1][n-1]위치로
 # 이동하는데 드는 최소 비용을 출력하는 프로그램을 작성하시오.

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

if __name__ == '__main__':
    for tc in range(int(input())):
        n = int(input())
        graph = []
        for i in range(n):
            graph.append(list(map(int, input().split())))

        # 7-2와 다르게 2차원이므로 최단거리 정보를 2차원으로 관리.
        distance = [[INF] * n for _ in range(n)]
        r, c = 0, 0
        distance[r][c] = graph[r][c]
        q = [(distance[r][c], r, c)]

        while q:
            dist, r, c = heapq.heappop(q)
            if distance[r][c] < dist:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < n and 0 <= nc < n:
                    if dist + graph[nr][nc] < distance[nr][nc]:
                        distance[nr][nc] = dist + graph[nr][nc]
                        heapq.heappush(q, (distance[nr][nc], nr, nc))

        print(distance[n-1][n-1])