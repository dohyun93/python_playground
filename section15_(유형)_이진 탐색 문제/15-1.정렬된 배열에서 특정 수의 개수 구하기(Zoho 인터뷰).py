# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 이 수열에서 x가 등장하는 횟수를 구하시오.
# 시간복잡도 O(logN) 으로 알고리즘 설계 하지 않으면 시간 초과.

from bisect import bisect_left, bisect_right
import sys

N, x = map(int, sys.stdin.readline().rsplit())
numbers = list(map(int, sys.stdin.readline().rsplit()))

def bisectAnswer():
    leftIdx = bisect_left(numbers, x)
    rightIdx = bisect_right(numbers, x)
    answer = rightIdx - leftIdx if rightIdx != leftIdx else -1
    print(answer)


# 아래는 정렬된 리스트에서 찾는 원소가 하나 일 때!
# 1. 반복문 이용
def iteration():
    answer = -1
    left, right = 0, len(numbers)-1
    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] == x:
            answer = mid
            break
        elif numbers[mid] < x:
            left = mid+1
            continue
        elif numbers[mid] > x:
            right = mid-1
            continue
    return answer


# 2. 재귀 이용
# 재귀 기본은 리턴이다. 그 뒤에 쭉 스택에서 실행되더라도
# 최초 호출 함수에서 리턴을 시켜 줘야 한다. 주의하자.
# 그리고 종료조건은 반드시 가장 최초에.
def recursive(left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if numbers[mid] == x:
        return mid
    elif numbers[mid] < x:
        return recursive(mid+1, right)
    elif numbers[mid] > x:
        return recursive(left, mid-1)

# 정렬된 리스트에서 다수 중복원소 있을 때 인덱스로 답 찾기
bisectAnswer()

# 정렬된 리스트에서 원소 하나 찾기.
# answer = iteration()
# answer = recursive(0, len(numbers)-1)
# print(answer)