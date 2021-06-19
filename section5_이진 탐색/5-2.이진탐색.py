# 이진 탐색은 start, mid, end 세 인덱스를 활용하여 O(logN)의 시간복잡도를 갖는 탐색 알고리즘이다.
# 구현 방법은 반복문을 활용해 찾을때까지 start, end를 이동해보는 것
# 또는 재귀함수로 구현하는 것이 있다.

N, target = map(int, input().split())
array = list(map(int, input().split()))

# 1. 재귀 함수
def recursive_binsearch(start, end):
    if start > end:
        return -2
    mid = (start+end) // 2 # -> 가운데 인덱스.
    if target == array[mid]:
        return mid
    elif target > array[mid]:
        return recursive_binsearch(mid+1, end)
    else:
        return recursive_binsearch(start, mid-1)

answer = recursive_binsearch(0, len(array)-1) + 1
if answer == -1:
    print(f"{target}은 array 에 없다.")
else:
    print(f"{target}은 array의 {answer}번째 요소다.")
# 2. 반복문

