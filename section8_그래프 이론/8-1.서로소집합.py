# V번의 탐색, M번의 find 혹은 union연산시 O(VM)
def findRootBad(parentList, x): # 루트노드를 매번 찾기만 함.
    if x != parentList[x]:
        return findRootBad(parentList, parentList[x])
    return x

# 부모리스트 갱신
# 바로 루트노드로 부모 정보를 갱신을 해주기 때문에, 더욱 효율적이다.
# findParent나 findRoot나 결국 루트노드를 탐색한다.
def findRootGood(parentList, x):
    if x != parentList[x]:
        parentList[x] = findRootGood(parentList, parentList[x])
    return parentList[x]

def union_parent(parentList, a, b):
    aParent = findRootGood(parentList, a)
    bParent = findRootGood(parentList, b)
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
    print(findRootGood(parentList, i), end=' ')

print("각 원소의 부모: ")
for i in range(1, v+1):
    print(parentList[i], end=' ')