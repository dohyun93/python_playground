def solution(stones, k):
    answer = 0
    road = [[-1, 0, 1]]
    for idx, number in enumerate(stones):
        road.append([idx, number, idx+2])
    road.append([len(stones), 0, -1])
    while True:
        quit = False
        # 첫 시작 위치를 정하기.
        curPos = -1
        for idx in range(1, k+1):
            if road[idx][1] != 0:
                curPos = idx
                break
        # 첫 발도 못내민 경우는 바로 종료.
        if curPos == -1:
            break
        while True:
            # 1. 종료지점 도달시 정답+1하고 반복.
            if curPos == len(stones)+1:
                break
            if road[curPos][1] > 0:
                road[curPos][1] -= 1
                # 1. 0이 되면 앞뒤 작업.
                if road[curPos][1] == 0:
                    road[road[curPos][0]][2] = road[curPos][2]
                    road[road[curPos][2]][0] = road[curPos][0]
                # 2. 이동
                distance = road[curPos][2] - curPos
                if distance <= k:
                    curPos = road[curPos][2]
                else:
                    quit = True
                    break

        if quit:
            break
        answer += 1
    return answer

# 0, 11인덱스는 끝지점.
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
result = solution(stones, k)
print(result)