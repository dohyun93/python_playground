# 선택정렬.
# 1. 바꿔줄 인덱스를 지정.
# 2. 1의 인덱스 숫자를 포함, 그 이후 숫자들 중 제일 작은 수 찾아 스왑
# 3. 스왑 후 인덱스 +1, 1단계로 다시 진행.
# 시간복잡도 : O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)