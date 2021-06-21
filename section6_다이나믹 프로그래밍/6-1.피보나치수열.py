import time

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
    elif 0 < x <= 2:
        return fibo[x]
    elif fibo[x] != 0:
        return fibo[x]
    fibo[x] = fibo_good(x-1) + fibo_good(x-2)
    return fibo[x]

x = int(input())

bad_start = time.time()
print(fibo_bad(x))
bad_end = time.time()
print(f"bad fibo took {bad_end - bad_start} ms")

good_start = time.time()
print(fibo_good(x))
good_end = time.time()
print(f"good fibo took {good_end - good_start} ms")
