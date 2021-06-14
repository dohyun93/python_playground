# 어떤 수 N이 1이 될 때까지 아래 두 과정 중 하나를 반복/선택하여 수행
# 최소한의 반복으로 1을 만드는데 드는 횟수는?

N, K = map(int, input().split())
answer = 0
while N != 1:
    if N % K == 0:
        N = int(N/K)
    else:
        N -= 1
    answer += 1

print(answer)