# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
# 균형잡힌 문자열
def balanceString(p):
    count = 0
    for charIdx in range(len(p)):
        if p[charIdx] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return charIdx # 균형잡히게하는 인덱스 반환

def rightString(p):
    count = 0 # 왼쪽 괄호 갯수
    for char in p:
        if char == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return True if count == 0 else False

def solution(p):
    answer = ''
    if p == '':
        return answer

    bal_index = balanceString(p)
    u = p[:bal_index+1]
    v = p[bal_index+1:]

    if rightString(u):
        answer = u + solution(v)

    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u_tmp = list(u[1:-1])
        for i in range(len(u_tmp)):
            if u_tmp[i] == '(':
                u_tmp[i] = ')'
            else:
                u_tmp[i] = '('
        answer += ''.join(u_tmp)

    return answer