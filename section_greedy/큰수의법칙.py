# N, M, K 입력 (2<=N<=1000 / 1 <=M <= 10000), K(1 <= K <=10000) , K <= M.
# N 개의 자연수 입력.
# 문제요약: N개의 수를 입력받고, 이 수중 M번 더하여 최대의 결과를 구하는 문제. 단, 연속되게 K번 동일 크기의 숫자를 더할 수는 없다.
# 전형적인 Greedy 문제로, 가장 큰 수와 그 다음 큰수만 있으면 된다. N이 2이상이기 때문에 정렬 후 가장큰 수, 그다음 큰수만 갖고 풀수있음.
import sys

N, M, K = map(int, input().split())
numbers = list(map(int, sys.stdin.readline().rsplit()))

sortedNumbers = sorted(numbers, reverse=True)
numOne, numTwo = sortedNumbers[0], sortedNumbers[1]

Z = numOne*K + numTwo
result = int(M/(K+1))*Z + numOne*(M%(K+1))
print(result)

# seqNum, m, answer = 0, 0, 0
# curSmall = False
# while True:
#     curNum = numOne if not curSmall else numTwo
#     m, seqNum = m+1, seqNum + 1
#     answer += curNum
#     print("m, seqNum, curNum: ", m, seqNum, curNum)
#     if m == M:
#         break
#     if seqNum == K: # K가 1일 때 계속 바꿔주는 역할.
#         curSmall = True if not curSmall else False
#         seqNum = 0
#         continue
#     if curSmall: # K가 1 초과일 때 다시 바로 첫 번째 큰수로 돌려주는 역할.
#         curSmall = False
#         seqNum = 0
# print(answer)

# print("m, seqNum, curNum: ", m, seqNum, curNum)
# 전체 루프 m / 그 안에서 k / 두 번째 작은수로 바꿔주는 처리 -> 3개 생각.