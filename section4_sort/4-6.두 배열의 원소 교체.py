import sys

# 길이가 N인 두 배열 A, B가 있다.
# 최대 K번 A와 B의 원소를 바꿔 A의 모든 원소합이 최대로 되게 할 때 A의 원소합의 최대값은?
# 전략> A 오름차순 정렬, B 내림차순 정렬.
#      1) 앞에서부터 A < B이면 교체. (K번까지 가능)
#      2) A == B면 그냥 continue. (count안하고.)
#      3) 만약 번까지 안갔는데 A > B면 종료.

N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().rsplit()))
B = list(map(int, sys.stdin.readline().rsplit()))

A = sorted(A)
B = sorted(B, reverse=True)

swapCnt = 0
answer = 0
for n in range(N):
    if swapCnt == K:
        break

    if A[n] < B[n]:
        A[n], B[n] = B[n], A[n]
        swapCnt += 1
    elif A[n] == B[n]:
        continue
    else:
        break

answer = sum(A)
print(answer)