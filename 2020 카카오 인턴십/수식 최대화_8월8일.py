# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
import re

def calc(signIdx, signsPermu, exList):
    if len(exList) == 1:
        return abs(int(exList[0]))
    nextExpression = []
    # 1. 숫자/기호 분리.
    digits = [ele for idx, ele in enumerate(exList) if idx % 2 == 0]
    signs = [ele for idx, ele in enumerate(exList) if idx % 2 == 1]

    # 2. 현재 순열에서 최우선 기호
    curSign = signsPermu[signIdx]
    for idx, sign in enumerate(signs):
        # 동일하면
        if sign == curSign:
            if not nextExpression: # 비어있으면 digits에 담긴 것으로 연산.
                if sign == '+':
                    nextExpression.append(str(int(digits[idx]) + int(digits[idx + 1])))
                elif sign == '-':
                    nextExpression.append(str(int(digits[idx]) - int(digits[idx + 1])))
                elif sign == '*':
                    nextExpression.append(str(int(digits[idx]) * int(digits[idx + 1])))
            else: # nextExpression 이 차있는 경우면 마지막 pop 한것과 digits[idx+1] 연산.
                lastDigit = nextExpression.pop()
                if sign == '+':
                    nextExpression.append(str(int(lastDigit) + int(digits[idx + 1])))
                elif sign == '-':
                    nextExpression.append(str(int(lastDigit) - int(digits[idx + 1])))
                elif sign == '*':
                    nextExpression.append(str(int(lastDigit) * int(digits[idx + 1])))

        # 불일치
        else:
            if len(nextExpression) == 0:
                nextExpression.append(digits[idx])
            nextExpression.append(sign)
            nextExpression.append(digits[idx + 1])
    return calc(signIdx + 1, signsPermu, nextExpression)

def solution(expression):
    answer = 0
    digits = re.split(r"[+*-]", expression)
    signs = re.split(r"[0-9]+", expression)
    signs = signs[1:-1]
    ex = []
    for idx in range(len(digits) + len(signs)):
        if idx % 2 == 0:
            ex.append(digits[idx//2])
        else:
            ex.append(signs[idx//2])
    uniqueSign = list(set(signs))
    for permu in list(permutations(uniqueSign)):
        answer = max(answer, calc(0, permu, ex))
    return answer