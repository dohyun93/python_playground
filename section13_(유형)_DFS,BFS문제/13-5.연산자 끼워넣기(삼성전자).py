N = int(input())
numbers = list(map(int, input().split()))
signs = list(map(int, input().split()))

maximum = -int(1e9)
minimum = int(1e9)

def backTracking(numcnt, sum, plus, minus, multi, divi):
    global maximum, minimum
    if numcnt == N:
        maximum = max(maximum, sum)
        minimum = min(minimum, sum)
        return
    if plus > 0:
        backTracking(numcnt+1, sum+numbers[numcnt], plus-1, minus, multi, divi)
    if minus > 0:
        backTracking(numcnt+1, sum-numbers[numcnt], plus, minus-1, multi, divi)
    if multi > 0:
        backTracking(numcnt+1, sum * numbers[numcnt], plus, minus, multi-1, divi)
    if divi > 0:
        if sum < 0:
            backTracking(numcnt+1, -(-sum//numbers[numcnt]), plus, minus, multi, divi-1)
        else:
            backTracking(numcnt + 1, sum // numbers[numcnt], plus, minus, multi, divi-1)

backTracking(1, numbers[0], signs[0], signs[1], signs[2], signs[3])
print(maximum)
print(minimum)