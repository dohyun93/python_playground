def solution(s):
    answer = 9999
    if len(s) == 1:
        answer = 1
        return answer
    for leng in range(1, int(len(s)/2) + 1):
        left = s[0:leng]
        same = 1
        substring = ""
        for idx in range(leng, len(s), leng):
            # 마지막 동일 또는 넘는경우 (끝)
            # 0123
            if idx + leng > len(s):
                right = s[idx:]
                if same > 1:
                    substring += str(same)
                substring += left
                substring += right
                break
            elif idx + leng == len(s):
                right = s[idx:]
                if left == right:
                    same += 1
                    substring += str(same)
                    substring += left
                    break
                else:
                    if same > 1:
                        substring += str(same)
                    substring += left
                    substring += right
                    break
            # 뒤에 아직 남은 경우
            else:
                right = s[idx:idx+leng]
                if left == right:
                    same += 1
                else:
                    if same > 1:
                        substring += str(same)
                        substring += left
                    else:
                        substring += left
                    left = right
                    same = 1

        answer = min(answer, len(substring))
        #print(substring)
        #print()
    return answer

#answer = solution("a")
#print(answer)