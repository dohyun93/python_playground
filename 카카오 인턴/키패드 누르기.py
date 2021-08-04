# https://programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = []
    pos = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    l_h = [3, 0]
    r_h = [3, 2]
    for n in numbers:
        lh_dist = abs(pos[n][0] - l_h[0]) + abs(pos[n][1] - l_h[1])
        rh_dist = abs(pos[n][0] - r_h[0]) + abs(pos[n][1] - r_h[1])
        # 1. 가장자리 줄 처리
        if pos[n][1] == 0:
            answer.append('L')
            l_h = pos[n]
            continue
        elif pos[n][1] == 2:
            answer.append('R')
            r_h = pos[n]
            continue
        # 2. 가운데 줄 처리
        elif lh_dist < rh_dist:
            answer.append('L')
            l_h = pos[n]
        elif rh_dist < lh_dist:
            answer.append('R')
            r_h = pos[n]
        elif lh_dist == rh_dist and hand == "right":
            answer.append('R')
            r_h = pos[n]
        elif lh_dist == rh_dist and hand == "left":
            answer.append('L')
            l_h = pos[n]
    answer = ''.join(answer)
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers, hand)
print(result)
