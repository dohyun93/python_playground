# 백준 - 감시 피하기
# dfs 백트래킹 문제로 할 수 있음.
# https://www.acmicpc.net/problem/18428
# combinations로 벽의 조합을 쓰지않고 풀이.

N = int(input())
graph = []
teacher = []
wall = []
result = "NO"

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for n in range(N):
    graph.append(list(map(str, input().split())))
    for j in range(N):
        if graph[n][j] == 'T':
            teacher.append((n, j))

def checkAnswer():
    global teacher, graph
    for t in teacher:
        for i in range(4):
            tr, tc = t
            while 0 <= tr < N and 0 <= tc < N:
                if graph[tr][tc] == 'S':
                    return False
                elif graph[tr][tc] == 'O':
                    break
                tr += dr[i]
                tc += dc[i]
    return True

def dfs(count):
    global graph, teacher, wall, result
    if count > 3:
        return
    if count == 3:
        if checkAnswer():
            result = "YES"
            return
        else:
            result = "NO"

    for i in range(N):
        for j in range(N):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                wall.append((i, j))
                dfs(count+1)
                if result == "YES":
                    return
                wall.remove((i, j))
                graph[i][j] = 'X'

dfs(0)
print(result)

# 참고 > 2d list 복사
# a를 b에 복사
# b = [row[:] for row in a]