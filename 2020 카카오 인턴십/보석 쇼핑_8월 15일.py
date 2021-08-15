# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict

def solution(gems):
    gem_dict = defaultdict(int) # gem의 인덱스 저장
    gnum = len(set(gems))

    left, right = 0, 0
    answer = [1, len(gems)]

    while right < len(gems):
        gem_dict[gems[right]] += 1
        right += 1

        # 이제 줄여나가는 스텝.
        if len(gem_dict) == gnum:
            while left < right:
                # 더 오른쪽으로 가면 이 gem은 이제 없기때문에 이 범위부터로 쳐야함.
                if gem_dict[gems[left]] == 1:
                    break
                gem_dict[gems[left]] -= 1
                left += 1 # 오른쪽으로 이동

            # 조건을 만족하는 현재 left, right의 범위가 기존 정답보다 더 적으면 정답 갱신.
            if answer[1] - answer[0] + 1 > right - left:
                answer = [left+1, right]
    return answer

# 아래 풀이는 O(N^2)의 시간복잡도이기 때문에 시간 초과.
# def solution(gems):
#     answer = []
#     unique_gems = set(gems)
#
#     # 탐색범위 시작~끝 길이
#     startLen = len(list(unique_gems))
#     endLen = len(gems)
#
#     for length in range(startLen, endLen+1): # O(N)
#         # 탐색 시작지점
#         done = False
#         for startIdx in range(0, endLen-length+1): # O(N)
#             curPart = set(gems[startIdx:startIdx+length])
#             if curPart == unique_gems:
#                 done = True
#                 # print("startIdx, length: ", startIdx, length)
#                 answer.append(startIdx+1)
#                 answer.append(startIdx+length)
#                 break
#         if done:
#             break
#     return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
result = solution(gems)

print(result)