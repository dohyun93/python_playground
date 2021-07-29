# 한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다. 각 집은 0번부터 N-1번까지의 번호로 구분됩니다.
# 모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일합니다.
# 예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해봅시다. 하루동안 이 가로등을 켜기 위한 비용은 7이 됩니다.
#
# 정부에서 일부 가로등을 비활성화 하여 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 합니다.
# 결과적으로 일부 가로등을 비활성화 하여 최대한 많은 금액을 절약하고자 합니다. 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화 하여
# 절약할 수 있는 최대 금액을 출력하는 프로그램을 개발하시오.
#
# 1 <= N <= 200,000
# N-1 <= M <= 200,000
#
# 출력: 일부 가로등을 비활성화 하여 절약할 수 있는 최대 금액 => MST에 포함하지 않는 간선들의 합.

# 이 문제는 크루스칼 알고리즘으로 MST를 만들고, 여기 포함되지 않는 간선들의 합을 출력하면 된다.
# 비용순으로 오름차순 정렬 후, 사이클을 만들지 않는다면 MST에 추가하고, 싸이클을 만든다면 answer += 간선비용 하면 됨.

import sys
input = sys.stdin.readline

def findRoot(root, a):
    if a != root[a]:
        root[a] = findRoot(root, root[a])
    return root[a]

def union(root, a, b):
    aRoot = findRoot(root, a)
    bRoot = findRoot(root, b)

    if aRoot < bRoot:
        root[bRoot] = aRoot
    else:
        root[aRoot] = bRoot

N, M = map(int, input().split())
INF = int(1e9)
adjInfo = []
answer = 0

for m in range(M):
    adjInfo.append(list(map(int, input().split())))

adjInfo = sorted(adjInfo, key=lambda x: x[2]) # 비용 오름차순으로 정렬
root = [n for n in range(N)]

for e in adjInfo:
    src, dst, cost = e
    # 싸이클 만들면 answer에 추가. 아니면 MST에 포함 (root union처리)
    if findRoot(root, src) != findRoot(root, dst):
        union(root, src, dst)
    else:
        answer += cost

print(answer)