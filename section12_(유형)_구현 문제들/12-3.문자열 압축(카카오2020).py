def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    for leng in range(1, len(s)//2+1):
        s_tmp = s
        curanswer = 0
        madeString = []
        while s_tmp:
            # python은 아래처럼 leng까지 슬라이싱 할 때, 범위 넘어도 괜찮다.
            # [5]길이에서 [2:1000]하면 [2]부터 [4]까지 가져옴.
            sliced = s_tmp[:leng]
            s_tmp = s_tmp[leng:]
            # 만든 스트링이 있다면
            if madeString:
                # 마지막 존재하는 것이랑 동일하면
                if madeString[-1][1] == sliced:
                    madeString[-1][0] += 1
                else:
                    madeString.append([1, sliced])
            # 없으면 1개정보 넣기
            else:
                madeString.append([1, sliced])
        for element in madeString:
            curanswer += len(element[1]) + (element[0] > 1) * len(str(element[0]))
        answer = min(curanswer, answer)
    return answer