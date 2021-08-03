# n은 1 이상 200 이하인 자연수입니다.
# weak의 길이는 1 이상 15 이하입니다.
# 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
# 취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
# weak의 원소는 0 이상 n - 1 이하인 정수입니다.
# dist의 길이는 1 이상 8 이하입니다.
# dist의 원소는 1 이상 100 이하인 자연수입니다.
# 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

# 시간복잡도는 15 * 8!
# 완전 탐색으로 해결 가능하다.

from itertools import permutations

def solution(n, weak, dist):
    extendedWeak = weak + [w+n for w in weak] # 전체 길이 n을 더해 선형으로 만듬.
    weakLen = len(weak)
    answer = []
    # 1. 점검 시작지점 지정
    for inWeakIdx, wholeWeakIdx in enumerate(weak):
        # 2. 보수작업 친구 순열
        for permu_friend_dist in permutations(dist):
            position = wholeWeakIdx
            curFriendNum = 1
            for thisFriendDist in permu_friend_dist:
                position += thisFriendDist
                # position이 점검 시작 위치(in extendedWeak) + weak 길이 이전 위치라면 투입필요.
                # 만약 같거나 큰경우 점검 완료상태.
                if position < extendedWeak[inWeakIdx+weakLen-1]:
                    curFriendNum += 1
                    position = [w for w in extendedWeak if w > position][0]
                else:
                    answer.append(curFriendNum)
                    break
    return min(answer) if answer else -1