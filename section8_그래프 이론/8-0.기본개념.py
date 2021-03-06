# 그래프 이론
# 0. 그래프 union, find 연산
#     union: (두 개의) 원소가 포함된 집합을 하나의 집합으로 합치는 연산
#     find : 원소가 속한 집합이 어떤 집합인지 찾는 연산
#
#     서로소 집합 자료구조 : 트리 자료구조를 이용해서 집합을 표현하는 서로소 집합 계산 알고리즘
#     1. union 연산 확인해서 서로 연결된 두 노드 A, B를 확인
#        A, B의 루트노트 A', B' 를 찾는다.
#        A'를 B'의 부모 노드로 설정한다. (B'가 A'를 가리킨다.)
#     2. 모든 union을 처리할 떄 까지 1번 과정을 반복한다.
#
# 이전 복습
# * 다익스트라 알고리즘 -> 한 지점에서 각 지점으로 가는 최단거리. distance[N]의 INF 초기화 및 인접 리스트를 이용해 그리디 알고리즘으로.
#   mean heap 자료구조를 사용해서 cost가 작은 것 먼저 탐색 -> import heapq. 시간복잡도는 O(ElogV)
# * 플로이드 워셜 알고리즘 -> 모든 지점에서 모든 지점으로 가는 최단거리. O(N^3).
#   인접 행렬을 이용해 DP 방법으로 푼다. dp[src][dst] = min(dp[src][dst], dp[src][k] + dp[k][dst]) 를 for k, src, dst 돌아서
#   O(N^3).

# 1. 신장트리 (Spanning tree)
#     하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프.
#
# 2. 크루스칼 알고리즘 - 그리디 알고리즘. - O(ElogE)
#     가장 적은 비용으로 모든 노드 연결하는 그리디 알고리즘.
#     1. 간선 데이터를 비용에 따라 오름차순 정렬
#     2. 간선 하나씩 확인하여 현재 간선이 사이클 발생하는지 확인
#         2-1. 사이클 발생x -> 최소신장트리에 포함
#         2-2. 사이클 발생o -> 최소신장트리에 미포함
#     3. 모든 간선에 대해 2번 과정 반복.
#
# 3. 위상정렬 알고리즘 - 큐 - O(V+E)
#     순서가 정해져 있는 일련의 작업을 차례로 수행해야 할 때 사용할 수 있는 알고리즘.
#     "방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것"
#     <algorithm>
#     진입차수가 0인 노드를 큐에 넣는다.
#     큐가 빌 때 까지 아래 과정 반복
#         큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#         새롭게 진입차수가 0이 된 노드를 큐에 넣는다.