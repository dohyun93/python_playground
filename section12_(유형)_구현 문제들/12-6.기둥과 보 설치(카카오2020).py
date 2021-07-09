PILLAR, BAR = 0, 1

def solution(n, build_frame):
    answer = []
    for b in build_frame:
        x, y, what, op = b
        if op == 1:
            if what == PILLAR: # 기둥 설치
                if checkPillar([x, y], answer):
                    answer.append(b[:3])
            else: # 바 설치
                if checkBar([x, y], answer):
                    answer.append(b[:3])
        else:
            tmp = answer.copy()
            tmp.remove(b[:3])
            deletePossible = True
            for t in tmp:
                x, y, what = t
                if what == PILLAR:
                    if not checkPillar([x, y], tmp):
                        deletePossible = False
                        break
                else:
                    if not checkBar([x, y], tmp):
                        deletePossible = False
                        break
            if deletePossible:
                answer = tmp.copy()
    answer.sort()
    return answer

def checkPillar(pillar_pos, answer):
    x, y = pillar_pos
    if y == 0:
        return True
    if [x, y-1, PILLAR] in answer or [x-1, y, BAR] in answer or [x, y, BAR] in answer:
        return True
    return False

def checkBar(bar_pos, answer):
    x, y = bar_pos
    if [x-1, y, BAR] in answer and [x+1, y, BAR] in answer:
        return True
    if [x, y-1, PILLAR] in answer or [x+1, y-1, PILLAR] in answer:
        return True
    return False