# 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
# 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
# 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
# 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
# 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
# 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
#      만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
# 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

# https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    # step1. - 알파벳 소문자로 str.lower()
    new_id = new_id.lower()

    # step2. - 알파벳 소문자/숫자/./_/- 제외하기
    splitted = re.split(r"[^0-9a-z._-]", new_id)
    new_id = ''.join(splitted)

    # step3. - .가 2번이상 -> .로 치환
    new_id = re.sub(r"[.]{2,}", '.', new_id)

    # step4. 양 끝 . 제거
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id.replace('.', '', 1)
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # step 5. new_id 빈 문자열이면 "a"로 처리
    if new_id == "":
        new_id = "a"

    # step 6.
    if len(new_id) >= 16:
        new_id = new_id[:15]
    new_id = new_id[:-1] if new_id[-1] == '.' else new_id

    # step 7.
    if len(new_id) <= 2:
        lastword = new_id[-1]
        while True:
            if len(new_id) == 3:
                break
            new_id = new_id + lastword

    return new_id