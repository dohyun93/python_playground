# 시작 위치를 weak에서 for로 돌리고
# 그 때, 각 친구들의 투입 순열을 넣어서 다 점검하기 전까지 투입된 친구 수들을 리스트에 저장.
from itertools import permutations # 순열
def solution(n, weak, dist):
    weak_len = len(weak)
    weak_extended = weak + [w+n for w in weak] # 선형으로 취급
    # (배운점1. list를 +로 이을 수 있다.)

    # ---------- | ===========
    # 위가 한 cycle , 위가 다음 cycle이나, 첫 번째 cycle의 모든 weak이 점검되었는지 확인 위해 다음 cycle까지 둠.
    answer = []
    for idx, startIdx in enumerate(weak):
        for friends_permu in permutations(dist):
            position = startIdx
            friendNum = 1 ##### 0->1로.
            for friend in friends_permu:
                position += friend
                if position < weak_extended[idx+weak_len-1]:
                    # 끝까지 도달하지 못한 경우
                    friendNum += 1 ##### 친구 추가투입. 이후 다음 friend for에서 아래 else조건만족해서
                                   # 끝나는 경우 추가처리가 되기때문에 여기서 +1.
                    # position을 남은 것들중 가장 가까운 weak지점으로 이동처리필요.
                    position = [w for w in weak_extended if w > position][0]
                    # ($$ 배운점 : list comprehention 뒤에 바로 인덱싱 넣을 수 있다.$$)
                else:
                    answer.append(friendNum)
                    break
    return min(answer) if answer else -1