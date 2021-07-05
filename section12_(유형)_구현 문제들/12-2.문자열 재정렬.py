# 알파벳 대문자와 숫자(0~9) 로만 구성된 문자열 입력
# 모든 알파벳을 오름차순으로 정렬해서 이어서 출력하고, 그 뒤에 모든 숫자를 더한 값을 이어서 출력하라.

S = input()

character = []
number = []

for i in S:
    if 'A' <= i <= 'Z':
        character.append(i)
    else:
        number.append(int(i))

character.sort()
character.append(str(sum(number)))

answer = ''.join(character)
print(answer)

# [input]
# AJKDLSI412K4JSJ9D
# [output]
# ADDIJJJKKLSS20