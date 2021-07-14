from collections import deque

dq = deque()
dq.append(3)
dq.append(1)
dq.append(4)

dq = sorted(dq)
print(dq)

# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
# 균형잡힌 문자열 - Kakao 2020
# 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
# 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
# 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#   4-3. ')'를 다시 붙입니다.
#   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#   4-5. 생성된 문자열을 반환합니다.

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
        u_tmp = list(u[1:-1]) # 문자열을 list로 만들어 활용 후 join으로 다시 문자열로.
        for i in range(len(u_tmp)):
            if u_tmp[i] == '(':
                u_tmp[i] = ')'
            else:
                u_tmp[i] = '('
        answer += ''.join(u_tmp)

    return answer
#####################################################
##### 13-5 연산자 끼워넣기 ##### -> permutations
from itertools import permutations
import sys

N = int(input())
number = list(map(int, sys.stdin.readline().rsplit()))
signs = list(map(int, sys.stdin.readline().rsplit()))
answersList = []
signList = []
for idx in range(len(signs)):
    for _ in range(signs[idx]):
        if idx == 0: # 덧셈
            signList.append('0')
        elif idx == 1: # 뺄셈
            signList.append('1')
        elif idx == 2: # 곱셈
            signList.append('2')
        else: # 나눗셈
            signList.append('3')

for permu in list(permutations(signList)):
    answer = number[0]
    for numIdx in range(1, len(number)):
        cursign = permu[numIdx-1]
        nextnum = number[numIdx]
        if answer < 0 and cursign =='3':
            answer = -(-answer // nextnum)
        elif cursign == '0':
            answer += nextnum
        elif cursign == '1':
            answer -= nextnum
        elif cursign == '2':
            answer *= nextnum
        elif answer >= 0 and cursign == '3':
            answer //= nextnum

    answersList.append(answer)

print(max(answersList))
print(min(answersList))
#####################################################