# N 점수가 입력되면 왼쪽 절반의 합과 오른쪽 절반의 합이 동일한 경우 '럭키 스트레이트' 기술 사용 가능.
# 입력받은 N점수가 기술사용 가능한 점수인지 확인.

N = list(map(int, input()))
left = N[:int(len(N)/2)]
right = N[int(len(N)/2):]

if sum(left) == sum(right):
    print("LUCKY")
else:
    print("READY")