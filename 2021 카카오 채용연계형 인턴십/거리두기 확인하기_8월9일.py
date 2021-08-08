# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1
# 가로/세로 헷갈려 헤멤. 꼼꼼히 풀자!

def isCovid(participant_pos, partition_pos):
    for i in range(0, len(participant_pos)-1):
        for j in range(i+1, len(participant_pos)):
            p1_r, p1_c = participant_pos[i][0], participant_pos[i][1]
            p2_r, p2_c = participant_pos[j][0], participant_pos[j][1]
            rowDist = abs(p1_r - p2_r)
            colDist = abs(p1_c - p2_c)
            manhatan_dist = rowDist + colDist
            if manhatan_dist == 1:
                return True
            elif manhatan_dist == 2:
                if colDist == 2:
                    # 가로
                    middle_c = (p1_c + p2_c) // 2
                    if (p1_r, middle_c) not in partition_pos:
                        return True
                elif rowDist == 2:
                    # 세로
                    middle_r = (p1_r + p2_r) // 2
                    if (middle_r, p1_c) not in partition_pos:
                        return True
                elif rowDist == 1 and colDist == 1:
                    # 직각
                    if (p1_r, p2_c) not in partition_pos or (p2_r, p1_c) not in partition_pos:
                        return True
    return False

def solution(places):
    answer = []
    # 1. places for 순회
    # 2. 각 place를 5x5 행렬로 매핑 -> 와중에 참가자 자리, 파티션 자리 추출
    # 3. 가로/세로/직각(4) 경우에 대해 만족하지 않으면 바로 정답에 0담고 break걸고 다음 place.

    # 핵심 -> 문자열 -> 리스트로 : list(str)
    # 번외 -> 리스트 -> 문자열: ''.join(리스트)

    for place in places:
        Room = []
        for row in place:
            Room.append(list(row))
        N = len(Room) # 숫자보단 이렇게 변수로
        participant_pos = []
        partition_pos = []
        for r in range(N):
            for c in range(N):
                if Room[r][c] == 'X':
                    partition_pos.append((r, c))
                elif Room[r][c] == 'P':
                    participant_pos.append((r, c))
        result = isCovid(participant_pos, partition_pos)
        answer.append(0 if result else 1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
answer = solution(places)
print(answer)