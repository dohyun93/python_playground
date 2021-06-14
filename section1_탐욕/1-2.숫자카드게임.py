import sys

N, M = map(int, input().split())
myMax = -1
for i in range(N):
    data = list(map(int, sys.stdin.readline().rsplit()))
    minVal = min(data) # O(logn)
    myMax = max(minVal, myMax)
print(myMax)