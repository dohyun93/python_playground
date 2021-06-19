array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 퀵 소트는 첫 번째 요소를 피벗으로 지정하고, 왼쪽에는 더 작은요소들, 오른쪽에는 더 큰 요소들을 배치하는 방식을 사용한다.
# 재귀적으로 풀 수 있으며, O(NlogN)이 소요된다.