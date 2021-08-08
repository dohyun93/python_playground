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
    myCombi = sorted(list(combi_set))

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
    print(f"2. 최대존재 페어 출력: {answer}")

    maxAnswer = []
    for ans in answer:
        length = len(ans[0])
        cnt = ans[1]
        if cnt == maxCourse[length]:
            maxAnswer.append(ans[0])
    print(f"maxAnswer: {maxAnswer}")
    print(f"maxCourse(dict): {maxCourse}")
    result = []
    # 4. 각 정답들 정렬, 정답간 순서 정렬
    for ans in maxAnswer:
        result.append(''.join(sorted(ans)))
    # XW, WX가 만들어지는 경우도 있음. 조합 만들 때 order 각각으로 만들 수 있는 조합이 처음에 담기기 때문에.
    # 그래서 메뉴 만든것을 내부적으로 정렬시켰을 때, 동일한 메뉴가 또 나올 수 있음.
    result = set(result)
    result = list(result)
    # 마지막으로 메뉴간 정렬까지.
    result.sort()
    return result

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
result = solution(orders, course)

# [참고]
# 아래처럼 문자열을 인자로 sorted를 하면 정렬된 문자들의 리스트를 반환함.
# 따라서 해당 리스트를 다시 ''.join의 인자로 전달해서 문자열로 다시 만들어줄 수 있음.
# 즉, 아래 방법은 문자열 내 문자들을 정렬된 문자열로 바꾸는 방법.
myString = "ZYX"
print(''.join(sorted(myString)))