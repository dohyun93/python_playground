import sys

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
sortedResult = sorted(arr, reverse=True)
for idx in sortedResult:
    print(idx, end=' ')

    
# list(map(int, input())) -> 연이어 들어오는 값 처리 (0000010203)
# list(map(int, input().split())) ------------------|-> ' ' 구분자로 들어오는 값들 처리.
# list(map(int, sys.stdin.readline().rsplit()))-----|