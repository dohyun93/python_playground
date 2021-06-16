def recursive(i):
    print(i, "번째 호출")
    if i == 10:
        print(i, "번째 호출 종료")
        return
    recursive(i+1)
    print(i, "번째 호출 종료")

recursive(1)