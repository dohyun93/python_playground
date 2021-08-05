# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N, stages):
    answer = []

    # 1. 1~N - 0 으로 사전 만들기
    map_stage_cnt = dict()
    for stage in range(1, N + 2): # N+1인게 stages에도 올 수 있고, 이는 계산에 활용되기에 N+2로 설정필요.
        map_stage_cnt[stage] = 0
    for stage in stages:
        map_stage_cnt[stage] += 1

    # stage s의 실패율:
    # map[s] / map[s] + map[s+1] ... + map[N]
    failure = []
    # (실패율, 스테이지) 저장

    for stage in range(1, N + 1): # 실패율은 1부터 N스테이지까지 계산하면 되지만,
        bunmo = 0
        for b in range(stage, N + 2): # 분모 계산시 N+1 스테이지 수도 계산필요하기때문에 N+2 지정필요.
            bunmo += map_stage_cnt[b]
        if bunmo != 0:
            fail = map_stage_cnt[stage] / bunmo
        else:
            fail = 0
        failure.append([fail, stage])


    failure = sorted(failure, key=lambda x: [-x[0], x[1]])
    for i in failure:
        answer.append(i[1])
    return answer