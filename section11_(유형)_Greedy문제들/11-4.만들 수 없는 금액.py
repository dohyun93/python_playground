import sys
N = int(input())
coins = list(map(int, sys.stdin.readline().rsplit()))
coins.sort()

target = 1
for curCoin in coins:
    # 타겟보다 다음 동전의 가치가 더 클 경우 앞에서 순차적으로 더해온 코인들의 값보다 1큰 수가 정답이다.
    if target < curCoin:
        break
    else:
        target += curCoin

print(target)