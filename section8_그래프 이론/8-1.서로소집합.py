def findParent(parentList, x):
    if x != parentList[x]:
        return findParent(parentList, parentList[x])
    return x

def findRoot(parentList, x):
    if x != parentList[x]:
        parentList[x] = findRoot(parentList, parentList[x])
    return parentList[x]

def union_parent(parentList, a, b):
    aParent = findRoot(parentList, a)
    bParent = findRoot(parentList, b)
    if aParent < bParent:
        parentList[b] = aParent
    else:
        parentList[a] = bParent

v, e = map(int, input().split())
parentList = [0] * (1+v)

for i in range(1, v+1):
    parentList[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parentList, a, b)

print("각 원소가 속한 집합(root): ")
for i in range(1, v+1):
    print(findRoot(parentList, i), end=' ')

print("각 원소의 부모: ")
for i in range(1, v+1):
    print(parentList[i], end=' ')