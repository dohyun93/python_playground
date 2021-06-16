# 재귀 1. -> 재귀함수는 내부적으로 스택의 동작방식을 따른다. -> 실제로 재귀함수는 메모리의 스택공간에 적재됨.
from collections import deque
def recursive(i):
    print(i, "번째 호출")
    if i == 10:
        print(i, "번째 호출 종료")
        return
    recursive(i+1)
    print(i, "번째 호출 종료")

recursive(1)

# 재귀 2. factorial.
# 2-1. 일반 for문.
normal = 1
for i in range(1, 6):
    normal *= i
print("5! =", normal)

# 2-2. 재귀.
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num *factorial(num-1)

print("5! =", factorial(5))

# DFS 구현.
Graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [0] * 9
def DFS(node):
    print(node, end=' ')
    visited[node] = 1
    for n_node in Graph[node]:
        if not visited[n_node]:
            DFS(n_node)
            # for 로 돌다가 조건 불만족시 추가진행 재귀가 없기 때문에
            # 재귀로 넣기 전의 상태로 돌아옴 -> pop의 효과가 있는 것.
DFS(1)
print()
# BFS 구현.
# BFS가 일반적으로 DFS보다 빠르게 동작한다.
# 추가로 deque 자료구조를 사용한다. (큐 구현위해서.)
# heapq 로 mean heap을 사용할 땐 이걸 사용.
visited = [False] * 9
def BFS(start, Graph, visited):
    q = deque([start])
    visited[start] = True
    while q:
        top = q.popleft()
        print(top, end=' ')
        for i in Graph[top]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

BFS(1, Graph, visited)