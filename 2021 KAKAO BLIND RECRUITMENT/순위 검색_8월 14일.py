# https://programmers.co.kr/learn/courses/30/lessons/72412

from collections import defaultdict
from itertools import combinations

def solution(info, queries):
    answer = []
    # 1. 모든 info 순열에 대해 딕셔너리 저장
    info_dict = defaultdict(list)
    for i in info:
        splitted = i.split()
        exceptScore = splitted[:-1]
        score = int(splitted[-1])
        for j in range(5):
            for c in combinations(exceptScore, j):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.split(' ')
        query_score = int(query[-1])
        query = query[:-1]

        for i in range(3):
            query.remove('and')
        while '-' in query:
            query.remove('-')
        tmp_q = ''.join(query)

        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= query_score:
                        end = mid
                    else:
                        start = mid+1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer




# 참고
# info = "java and backend and junior and pizza 100"
# splittedList = info.split(" and ")
# print(splittedList)
# ## 문자열.split(구분자) 는 분리된 문자열들의 리스트 반환함.
# 
# # 마지막 것은 " and " 로 구분되지 않으므로 뺀 뒤에 스페이스로 분리한것을
# # extend로 원소만 넣어준다.
# last = splittedList.pop()
# 
# splittedList.extend(last.split(" "))
# print(splittedList)

letters = "kwondohyun"
myDict = defaultdict(int)
for char in letters:
    myDict[char] += 1
print(myDict.items())

# [배운점 2]
# defaultdict으로 value의 기본 자료형을 지정할 수 있고,
# key가 없더라도 산술 연산이 가능하다.