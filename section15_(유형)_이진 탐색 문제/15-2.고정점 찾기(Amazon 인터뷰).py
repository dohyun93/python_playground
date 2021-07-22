n = int(input())
data = list(map(int, input().split()))

def rec(left, right):
    if left > right:
        return -1
    mid = (left+right)//2
    if data[mid] == mid:
        return mid
    else:
        leftAns = rec(left, mid-1)
        rightAns = rec(mid+1, right)
        return leftAns if leftAns != -1 else rightAns

answer = rec(0, len(data)-1)
print(answer)