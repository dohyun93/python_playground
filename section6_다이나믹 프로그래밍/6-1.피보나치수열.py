import time

def fibo_bad(x):
    if x == 1 or x == 2:
        return 1
    return fibo_bad(x-1) + fibo_bad(x-2)

# print(fibo_bad(10)) # 이런 방식은 함수호출의 기하급수적 증가를 야기함.

fibo = [0] * 100
fibo[1], fibo[2] = 1, 1

def fibo_topdown(x):
    if x <= 0:
        return -1
    elif 0 < x <= 2:
        return fibo[x]
    elif fibo[x] != 0:
        return fibo[x]
    fibo[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return fibo[x]

def fibo_botomup(x):
    if x <= 0:
        return -1
    elif 0 < x <= 2:
        return fibo[x]
    else:
        if fibo[x] != 0:
            return fibo[x]

        for i in range(3, x+1):
            fibo[i] = fibo(i-1) + fibo(i-2)
        return fibo[x]

x = int(input())

bad_start = time.time()
print(fibo_bad(x))
bad_end = time.time()
print(f"bad fibo took {bad_end - bad_start} ms")

good_start = time.time()
print(fibo_topdown(x))
good_end = time.time()
print(f"good fibo took {good_end - good_start} ms")

good_start = time.time()
print(fibo_botomup(x))
good_end = time.time()
print(f"fibo botom up took {good_end - good_start} ms")
