# https://programmers.co.kr/learn/courses/30/lessons/64064?language=python3

from itertools import permutations

def satisfy(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(banned_id[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    user_permutations = list(permutations(user_id, len(banned_id)))
    # 조합으로 하면 만족하는 경우 satisfy함수에서 못찾아낼 수 있다.
    # 모든 순열의 경우에 대해 탐색해보고 만족하면 그 순열을 집합화해서 기존 유무 확인하여야 한다.
    banSet = []
    for users in user_permutations:
        if not satisfy(users, banned_id):
            continue

        else:
            users = set(users)
            # (A, B, C), (A, C, B), (B, A, C), (B, C, A), (C, A, B), (C, B, A)
            # 같은 user 모두 동일취급
            if users not in banSet:
                banSet.append(users)
    return len(banSet)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

result = solution(user_id, banned_id)
print(result)