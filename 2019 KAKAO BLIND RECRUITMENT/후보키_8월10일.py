from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    combiList = []
    for select in range(1, col+1):
        combiList.extend(list(combinations([i for i in range(col)], select)))

    unique = []
    for combi in combiList:
        subset = set()
        for r in range(row):
            subset.add(tuple(relation[r][k] for k in combi)) # 이건 첨보네

        if len(subset) == row: unique.append(combi)

    answers = []
    for u in unique:
        tuple2set = set(u)
        satisfy = True

        for a in answers:
            if a.issubset(tuple2set):
                satisfy = False
                break
        if satisfy: answers.append(tuple2set)

    return len(answers)