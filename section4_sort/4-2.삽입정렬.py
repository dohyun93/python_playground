# 삽입정렬.
# 최초 [1]부터 탐색. 그 앞의 요소들은 정렬되어있다고 가정.
# pseudo code
# i := 1 ~ len-1
#    j := i ~> 0, -1.
#        arr[j] < arr[j-1] : swap. else: break. --> 더 앞의 요소들은 이미 작은 것들로 정렬되어있기 때문.
# 시간복잡도: O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)