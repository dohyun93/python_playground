def rotate(key):
    m = len(key)
    key_ = [[0]*m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            key_[c][m-r-1] = key[r][c]
    return key_

def check(lock_padding):
    n = len(lock_padding) // 3
    for r in range(n, n*2):
        for c in range(n, n*2):
            if lock_padding[r][c] != 1:
                return False
    return True

# 자물쇠에 열쇠 넣기
def KeyIn(lock_padding, key):
    n = len(lock_padding) // 3
    # r, c는 비교 시작할 lock_padding의 위치
    # i, j는 r, c로부터 시작할 key요소의 위치
    for r in range(n*2):
        for c in range(n*2):
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[r+i][c+j] += key[i][j]
            if check(lock_padding):
                return True
            for i in range(len(key)):
                for j in range(len(key)):
                    lock_padding[r + i][c + j] -= key[i][j]
    return False

def solution(key, lock):
    answer = False
    n = len(lock)
    lock_padding = [[0] * (n*3) for _ in range(3*n)]
    for r in range(n):
        for c in range(n):
            lock_padding[r+n][c+n] = lock[r][c]
    rotateCount = 0
    while True:
        answer = KeyIn(lock_padding, key)
        if answer or rotateCount == 3:
            break
        else:
            rotateCount += 1
            key = rotate(key)
    return answer