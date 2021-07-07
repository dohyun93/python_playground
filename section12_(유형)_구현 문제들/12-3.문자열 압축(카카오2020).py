def solution(s):
    answer = 1001
    if len(s) == 1:
        return 1
    for leng in range(1, len(s)//2+1):
        sliced = s[:leng]
        s_copy = s[leng:]
        makeStrings = [[1, sliced]]

        while s_copy:
            sliced = s_copy[:leng]
            if makeStrings[-1][1] == sliced:
                makeStrings[-1][0] += 1
                s_copy = s_copy[leng:]
            else:
                makeStrings.append([1, sliced])
                s_copy = s_copy[leng:]
        curAnswer = 0
        for element in makeStrings:
            curAnswer += len(element[1]) + (element[0] > 1) * len(str(element[0]))
        answer = min(answer, curAnswer)
    return answer