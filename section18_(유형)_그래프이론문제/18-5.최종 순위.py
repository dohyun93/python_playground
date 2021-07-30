from collections import deque

for tc in range(int(input())):
    n = int(input())
    indegree = [0]*(n+1)
    graph = [[False] * (n+1) for _ in range(n+1)]
    data = list(map(int, input()))
    for i in range(n):
        for j in range(i+1, n):
            # 1. 자기보다 순위가 낮았던 팀 j 가리키기.
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 알고리즘 시작
    # [특이 케이스]
    # 1. 사이클이 발생하는 경우, 2. 위상 정렬의 결과가 1개가 아니라 여러개인 경우
    # 위 두가지 해당없다면 오직 하나의 경우만 정답 존재.

    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True # 위상정렬 결과가 하나인 여부
    cycle = False  # 그래프 내 사이클이 존재하는 여부

    for i in range(n):
        # 큐가 빈 경우는 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)


    if cycle:# 사이클이 발생해서 데이터에 일관성이 없어 순위를 정할 수 없다.
        print("IMPOSSIBLE")
    elif not certain: # 정답이 여러개여서 확실한 순위를 정할 수 없다.
        print("?")
    else:
        for i in result:
            print(i, end = ' ')
        print()