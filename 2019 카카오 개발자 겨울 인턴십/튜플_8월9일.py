# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    S = s[2:-2].split('},{')
    wholeSet = []
    for element in S:
        wholeSet.append(set(element.split(',')))
    wholeSet = sorted(wholeSet, key=lambda x: len(x))

    before = set()
    for element in wholeSet:
        minus = element - before
        answer.append(list(minus)[0])
        before = before | minus
    ans = [int(i) for i in answer]
    return ans