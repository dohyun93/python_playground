# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nameDict = dict()

    # 1. 존재하는 모든 uid 파악, 이름 매칭
    for element in record:
        splitted = element.split()
        if len(splitted) == 2:
            ins, uid = splitted

        elif len(splitted) == 3:
            ins, uid, name = splitted
            nameDict[uid] = name

    # 2. 출력
    for element in record:
        splitted = element.split()
        if len(splitted) == 2:
            leftName = nameDict[splitted[1]]
            answer.append(leftName + "님이 나갔습니다.")
        elif len(splitted) == 3:
            if splitted[0] == "Enter":
                enterName = nameDict[splitted[1]]
                answer.append(enterName + "님이 들어왔습니다.")
            elif splitted[0] == "Change":
                continue

    return answer