# 못생긴 수는 오직 2, 3, 5만을 소인수로 갖는 수를 의미한다.
# 1은 못생긴 수라고 할 때 n번째 못생긴 수를 구하시오.

n = int(input())
ugly = [0] * n
ugly[0] = 1

idx2, idx3, idx5 = 0, 0, 0 # 곱해야 할 각 수(2, 3, 5)의 피연산 인덱스.
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    ugly[i] = min(next2, next3, next5)
    if ugly[i] == next2:
        idx2 += 1
        next2 = ugly[idx2] * 2
    if ugly[i] == next3:
        idx3 += 1
        next3 = ugly[idx3] * 3
    if ugly[i] == next5:
        idx5 += 1
        next5 = ugly[idx5] * 5

print(ugly)

print(ugly[n-1])