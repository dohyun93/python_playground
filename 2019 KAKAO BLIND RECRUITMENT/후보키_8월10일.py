from itertools import combinations

def solution(relation):
    answer = 0
    # 문제 풀이 전략
    # 1. 컬럼 데이터들을 따로 뽑아둔다.
    # 2. 조합으로 선택할 열들을 고른다. (1개 조합 ~ 컬럼의 개수 조합)
    # 3. 만약 3개 (0, 2, 4 idx의 열)를 골랐다면 해당 열의 데이터들을 1번을 활용해
    # 리스트에 다 넣어주고 (페어로), 그 개수가 집합으로 변경한 것과 동일한지 계산한다.
    # 만약 가능하다면 answer +1.
    colNum = len(relation[0])
    colData = [[] for _ in range(colNum)]
    for tuple in relation:
        for j in range(len(tuple)):
            colData[j].append(tuple[j])
    print(colData)

    colidx = [i for i in range(colNum)]
    for selection in range(1, colNum+1):
        # 1. 1개부터 컬럼전체 까지
        # 조사한 조합이 유일성을 만족하는 경우, 정답의 조합들 in 현재 조합이라면 추가하지 않음.
        # 아니라면 추가.
        for colCombi in list(combinations(colidx, selection)):
            # 2. selection개수만큼 조합 뽑기
            print(colCombi)



    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)

colidx = [i for i in range(0, 4)]
for combi in range(1, 4):
    curCombi = list(combinations(colidx, combi))
    if combi == 1:
        print("1일떄: ", curCombi)
        print(curCombi)
        print(curCombi[0][0])
        print(curCombi[1][0])
        print(curCombi[2][0])
        print(curCombi[3][0])

