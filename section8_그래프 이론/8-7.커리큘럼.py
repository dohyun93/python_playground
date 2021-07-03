# N개 강의를 듣고자 한다.
# 각 강의는 강의시간이 있으며, 선수과목이 존재할 수 있는데, 이 강의를 들어야 수강이 가능하다.
# 강의는 동시에 수강이 가능하다고 가정하였을 때, 모든 강의를 수강하기까지 소요되는 최소 시간은?
# 순서가 있는 유향그래프 그리기 -> 위상정렬 알고리즘 O(V + E)

from collections import deque
import copy # for deepcopy

N = int(input())
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)

for node in range(1, N+1):
    data = list(map(int, input().split()))
    time[node] = data[0]
    for x in data[1:-1]:
        indegree[node] += 1
        graph[x].append(node)

def topologysort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        for dst in graph[cur]:
            # dst까지 소요시간은 구한 값 vs 현재까지 값+dst시간값 중 큰 값.
            # max로 해야 이전 강의수강시간을 더한값과 현재값 비교를 통해 더 큰 전자의 시간을 정답리스트에 갱신할 수 있다.
            result[dst] = max(result[dst], result[cur] + time[dst])
            indegree[dst] -= 1
            if indegree[dst] == 0:
                q.append(dst)

    for i in range(1, N+1):
        print(result[i])

topologysort()

# [input]
# 노드 갯수
# 강의시간, 선수과목(들), -1은 끝 표시
#
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1
#
# [output]
# 각 강의를 수강하는데 걸리는 최소 시간
#
# 10
# 20
# 14
# 18
# 17