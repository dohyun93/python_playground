# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []
    # 1. 현재 주문들로 course의 갯수만큼 조합 구하기
    combi_set = set()
    for o in orders:
        for c in course:
            curcombi = list(combinations(o, c)) # [('a', 'b'), ('a', 'c'), ...)] 이런식임.
            for idx in range(len(curcombi)):
                combi_set.add(''.join(curcombi[idx]))
    # 모든 조합 담음.
    myCombi = list(combi_set)

    # 2. 각 조합을 순회하면서 조합내 음식이 주문에서 몇개 등장하는지 카운트 후, 2개 이상이면 정답에 일단 넣기
    # o 내 모두 조합이 있고, 그런 경우가 orders 통틀어서 2개 이상이면 넣기.
    for combi in myCombi:
        combi_cnt = 0 # orders에서 이 조합 등장 횟수
        for o in orders:
            Exist = True
            for char in combi:
                if char not in o:
                    Exist = False
                    break
            if Exist:
                combi_cnt += 1
        if combi_cnt >= 2:
            answer.append((combi, combi_cnt))

    # 3. course개 조합들 중 가장 많은 answer만 남기기.
    maxCourse = dict() # course와 인덱스 동일한 경우에 대해 가장 많은 등장횟수 저장.
    for c in (course):
        maxCourse[c] = 0
        for ans in answer:
            if len(ans[0]) == c:
                maxCourse[c] = max(maxCourse[c], ans[1])

    maxAnswer = []
    for ans in answer:
        length = len(ans[0])
        cnt = ans[1]
        if cnt == maxCourse[length]:
            maxAnswer.append(ans[0])
    result = []
    # 4. 각 정답들 정렬, 정답간 순서 정렬
    for ans in maxAnswer:
        result.append(''.join(sorted(ans)))
    result = set(result)
    result = list(result)
    result.sort()
    return result

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
result = solution(orders, course)
print(result)

# 맨 위에서 집합으로 처리하는데 왜 중복도 나왔는지?
# 49라인 sorted 결과 조인부분.