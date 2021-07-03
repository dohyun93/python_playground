def findRoot(roots, a):
    if roots[a] != a:
        roots[a] = findRoot(roots, roots[a])
    return roots[a]

def union(roots, a, b):
    aRoot = findRoot(roots, a)
    bRoot = findRoot(roots, b)

    if aRoot < bRoot:
        roots[bRoot] = aRoot
    else:
        roots[aRoot] = bRoot

# 같은 팀이다 ? 같은 루트노드를 갖는다.

N, M = map(int, input().split())
roots = [0] * (N+1)

# 0~N번까지 학생. 총 N+1명.
for i in range(N+1):
    roots[i] = i

answer = []
for m in range(M):
    op, a, b = map(int, input().split())
    if op == 0:
        union(roots, a, b)
    elif op == 1:
        aRoot = findRoot(roots, a)
        bRoot = findRoot(roots, b)
        if aRoot == bRoot:
            answer.append("YES")
        else:
            answer.append("NO")

for i in answer:
    print(i)

# [input]
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# [output]
# NO
# NO
# YES