# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

from itertools import permutations

def check(permu, banned_id):
    for idx, p in enumerate(permu):
        curBan = banned_id[idx]
        if len(p) != len(curBan):
            return False
        for j in range(len(curBan)):
            if curBan[j] == '*':
                continue
            else:
                if curBan[j] != p[j]:
                    return False
    return True


def solution(user_id, banned_id):
    answer = []
    banned_num = len(banned_id)

    for permu in list(permutations(user_id, banned_num)):
        if check(permu, banned_id):
            p_set = set(permu)
            if p_set not in answer:
                answer.append(p_set)
    return len(answer)


# fr*d* -> frodo, fradi
# *rodo -> frodo, crodo
# ****** -> abc123, frodoc
# ****** -> abc123, frodoc

# frodo / crodo / abc123 / frodoc
# frodo / crodo / frodoc / abc123 -> 동일하게 취급. 즉 순열들로 비교하되, 마지막에 넣을 때는
# set으로 변화시킨 것이 정답리스트에 포함되어있는지 확인 후 넣음.