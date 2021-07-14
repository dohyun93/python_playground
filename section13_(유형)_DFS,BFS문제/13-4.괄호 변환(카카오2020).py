def balancedIdx(p):
    leftCnt = 0
    rightCnt = 0
    for idx in range(len(p)):
        if p[idx] == '(':
            leftCnt += 1
        else:
            rightCnt += 1

        if leftCnt == rightCnt:
            return idx
    return -1 # not reachable under p constraint. (p is always balancedString)

def isAlright(p):
    sum = 0
    for char in p:
        if char == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False
    return True if sum == 0 else False

def reversedAndExtract(p):
    reversed = ''
    for char in p:
        if char == '(':
            reversed += ')'
        else:
            reversed += '('

    return reversed[1:-1]

def solution(p):
    answer = ''
    if p == '':
        return answer

    balIdx = balancedIdx(p)
    u, v = p[:balIdx+1], p[balIdx+1:]

    if isAlright(u):
        answer = u + solution(v)

    else:
        empt = '('
        empt += solution(v)
        empt += ')'
        empt += reversedAndExtract(u)
        return empt

    return answer

print(solution("(()))("))