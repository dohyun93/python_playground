# string은 0또는1로 이루어진 문자열.
# 1과 0의 군을 나누고, 더 적은 군을 갖는 집단의 군 수를 구하면 된다.
# 이 수가 곧 뒤집어주는 횟수고 그것이 답이다.

string = input()

if len(string) == 0:
    print(0)

else:
    curNum = string[0]
    zeroGroup = 0
    oneGroup = 0

    # 먼저 현재 숫자 그룹 수 +1. 이렇게 했기때문에 다음에 새로등장한 그룹수부터 카운트.
    if curNum == '0':
        zeroGroup = 1
    else:
        oneGroup = 1

    for i in string[1:]:
        if i != curNum:
            # 새 숫자가 1이면 1로 바꿔주고, 1 그룹수 +1.
            if curNum == '0':
                curNum = '1'
                oneGroup += 1
            # 새 숫자가 0이면 0으로 바꿔주고, 0 그룹수 +1.
            else:
                curNum = '0'
                zeroGroup += 1

    answer = min(zeroGroup, oneGroup) # 더 적은 수의 그룹만큼 뒤집어주면 됨.
    print(answer)