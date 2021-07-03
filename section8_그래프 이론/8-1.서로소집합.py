def findRoot_1(parent, x):
    if parent[x] != x:
        return findRoot_1(parent, parent[x])
    return parent[x]

# 경로 압축. 부모 테이블에 루트정보를 넣음.
# 그래서 위 함수에서 부모테이블의 정보와 다름. (부모 테이블(위) vs 루트 테이블(아래))
def findRoot_2(parent, x):
    if parent[x] != x:
        parent[x] = findRoot_2(parent, parent[x])
    return parent[x]

# findRoot_1은 루트노드를 찾을 수는 있으나, 부모 정보를 갱신해주지는 않음.

def makeUnion(parent, a, b):
    # makeUnion은 두 노드의 루트노드를 비교해서 더 작은 루트노드를 다른 노드의 부모로 지정한다.
    # 루트노드를 그룹으로 생각하고 그루핑을 한다고 생각하면 편함.
    aRoot = findRoot_2(parent, a)
    bRoot = findRoot_2(parent, b)

    # a가 속한 집합으로 b를 union해야 함.
    # b루트의 루트값(=b루트)을 a의 루트값으로 바꿔야한다.
    if aRoot < bRoot:
        parent[bRoot] = aRoot
    else:
        parent[aRoot] = bRoot


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    makeUnion(parent, a, b)

print('각 원소의 루트노드')
for i in range(1, v+1):
    #print(findRoot_1(parent, i), end=' ')
    print(findRoot_2(parent, i), end=' ')

print('\n각 원소의 부모노드')
for i in range(1, v+1):
    print(parent[i], end= ' ')
#[input]
# 6 5
# 1 4
# 2 3
# 2 4
# 5 6
# 2 3

#[output]
# 각 원소의 루트노드
# 1 1 1 1 5 5
# 각 원소의 부모노드
# 1 1 1 1 5 5