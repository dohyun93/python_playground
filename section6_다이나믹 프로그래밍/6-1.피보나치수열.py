def fibo_bad(x):
    if x == 1 or x == 2:
        return 1
    return fibo_bad(x-1) + fibo_bad(x-2)

# print(fibo_bad(10)) # 이런 방식은 함수호출의 기하급수적 증가를 야기함.

fibo = [0] * 100
fibo[1], fibo[2] = 1, 1

def fibo_good(x):
    if x <= 0:
        return -1
    if 0 < x <= 2:
        return fibo[x]

    for i in range(3, x):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
        print(f"fibo({i}) : {fibo[i]}")
    return fibo[x - 1] + fibo[x - 2]

x = int(input())
print(fibo_good(x))