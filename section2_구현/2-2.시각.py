# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중 3이 하나라도 들어가는 모든 경우의 수를 구한다:

N = int(input())
answer = 0
for h in range(N+1):
    for m in range(60):
        for s in range(60):
            stringify = []
            stringify.append(str(h))
            stringify.append(str(m))
            stringify.append(str(s)) # 여기까지는 [h, m, s] 이럼.
            stringify = ''.join(stringify) # ''(구분자없이).join해서 하나의 문자열로.
            if '3' in stringify:
                answer += 1
print(answer)