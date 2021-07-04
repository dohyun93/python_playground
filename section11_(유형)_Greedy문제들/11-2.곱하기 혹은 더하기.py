number = list(map(int, input()))

# 주어진 정수로 만들 수 있는 가장 큰 수를 구하시오.
# 연산은 + 혹은 x 만 할 수 있고, 앞에서부터 순차적으로만 할 수 있다.
# 피연산자 중 하나라도 0 또는 1이 있으면 -> +.
# 그 외인 경우 x.

answer = number[0]

if len(number) == 1:
    print(answer)

else:
    for num in number[1:]:
        if answer <= 1 or num <= 1:
            answer += num
        else:
            answer *= num

print(answer)