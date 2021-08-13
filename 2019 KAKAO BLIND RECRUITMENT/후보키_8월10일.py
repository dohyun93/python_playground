from itertools import combinations


def solution(relation):
    # 컬럼의 개수, 행의 개수, 컬럼 리스트(인덱스로 표현함)
    n_col = len(relation[0])
    n_row = len(relation)
    list_col = [i for i in range(n_col)]
    # 컬럼 리스트로 후보키 조합 만들기
    # 주의사항 : list를 [] 없이 추가하고 싶을 때는 append 대신 extend 사용!
    combs_col = []
    for i in range(1, n_col + 1):
        combs_col.extend(list(combinations(list_col, i)))
    # print(combs_col)

    # 유일성 : 유일하게 식별되어야 함 =&gt; 해당 컬럼 안에 중복된 값이 없어야 한다.
    uniques = []
    for i in combs_col:
        key = set()  # key : {} 주의 : append 대신 add를 이용
        for j in range(n_row):
            key.add(tuple(relation[j][k] for k in i))  # set을 이용하므로 tuple 사용
            # print(key)
        if len(key) == n_row: uniques.append(i)
    # print(uniques)

    answer = []
    # 최소성 : uniques에 포함된 부분집합 안에 부분집합이 포함되면 안됨.
    for i in uniques:
        sub = set(i)
        # print(sub)
        check = True
        for j in answer:
            if j.issubset(sub):  # answer에 들어가있는 부분집합이 sub 안에 포함될 경우, sub 미포함.
                check = False
        if check == True: answer.append(sub)
    # print(answer)
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
result = solution(relation)
print(result)