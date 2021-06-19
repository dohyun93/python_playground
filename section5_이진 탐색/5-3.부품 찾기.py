# N이 주어지고, N개의 숫자를 입력
# 그 후 ,  M을 입력하고 M개의 숫자를 입력. M개 숫자가 N개 숫자 중 포함되어있으면 yes, 아니면 no 출력.
# 방법: set / 이진탐색
import sys

N = int(input())
nItems = list(map(int, sys.stdin.readline().rsplit()))
M = int(input())
mItems = list(map(int, sys.stdin.readline().rsplit()))

# 방법 1. 집합으로 존재하는 원소인지만 판별. -> in 키워드로 집합 확인.
nItemsSet = set(nItems)
for m in range(len(mItems)):
    if mItems[m] in nItemsSet:
        print("yes", end=' ')
    else:
        print("no", end=' ')

print()
# 방법 2. 이진탐색.
sortedNItems = sorted(nItems)
def binary_search_recursive(start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if target == sortedNItems[mid]:
        return mid
    elif target < mid:
        return binary_search_recursive(start, mid-1, target)
    else:
        return binary_search_recursive(mid+1, end, target)

for m in mItems:
    result = binary_search_recursive(0, len(sortedNItems)-1, m)
    if result != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')