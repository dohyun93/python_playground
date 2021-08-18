###################################
# 1. 문자열들로 이뤄진 리스트에서 중복 제거
print("< 1. 문자열들로 이뤄진 리스트에서 중복 제거 > ")

list1 = ["kwon", "kwon", "park", "kim", "jung"]
print(f"기존 문자열: {list1}")
list2 = list(set(list1))
print(f"중복제거 문자열: {list2}")
print()
print()

# *** 출력 ***
# 1. 문자열들로 이뤄진 리스트에서 중복 제거
# 기존 문자열: ['kwon', 'kwon', 'park', 'kim', 'jung']
# 중복제거 문자열: ['kwon', 'park', 'jung', 'kim']




###################################
# 2. defaultdict vs dict
# dict은 키에 대해 미리 밸류가 지정이 되어야 키 인덱스에 대한 밸류를 반환할 수 있다.
# 하지만 defaultdict은 미리 키가 없더라도 default로 지정된 데이터 타입의 기본값으로 밸류를 반환할 수 있다.
# 키에 대해 자료형별 value의 default값.
# int -> 0
# float -> 0.0
# set -> set()
# dict -> {}
# list -> []

print("< 2. defaultdict의 활용 >")

from collections import defaultdict

myDefDict = defaultdict(list) # value의 기본타입 지정 가능.

names = [("kwon", "dohyun"), ("kim", "dohyun"), ("park", "dohyun"), ("jung", "donghyong"), ("jung", "kilsun")]
print(names)
for name in names:
    myDefDict[name[0]].append(name[1]) # 키에 대해 default타입인 list 밸류에 추가.

print(list(myDefDict.items()))
print()
print()

mydict2 = dict()
# print(mydict2[2]) -> 에러 발생. defaultdict은 지정한 자료형의 기본타입으로 할당하여 에러 미발생.
# *** 출력 ***
# 2. defaultdict의 활용
# [('kwon', 'dohyun'), ('kim', 'dohyun'), ('park', 'dohyun'), ('jung', 'donghyong'), ('jung', 'kilsun')]
# [('kwon', ['dohyun']), ('kim', ['dohyun']), ('park', ['dohyun']), ('jung', ['donghyong', 'kilsun'])]





###################################
print("< 3. 집합 내 원소 추가는 리스트 안됨. 튜플만 가능 >")
set1 = set()
# set1.add([1, 2, 3]) # TypeError: unhashable type: 'list'
# dict = defaultdict(int) # TypeError: unhashable type: 'collections.defaultdict'
# dict = dict()
# dict[2] = 3
# set1.add(dict)      #TypeError: unhashable type: 'dict'

combination = [1, 3, 5]
from itertools import combinations
for select in range(len(combination)):
    for c in combinations(combination, select):
        set1.add(c)
print("조합으로 만든 리스트의 튜플원소들 집합에 넣기: ", set1)
if () in set1:
    print("if () in set1조건 만족해서 () 튜플도 있다. 길이는 ", len(()))
if (1,) in set1:
    print("if (1,) in set1조건 만족해서 (1,) 튜플도 있다. 길이는 ", len((1,)))
print()
print()
# *** 출력 ***
# 3. 집합 내 원소 추가는 리스트 안됨. 튜플만 가능.
# 조합으로 만든 리스트의 튜플원소들 집합에 넣기:  {(5,), (1, 5), (1,), (3,), (), (1, 3), (3, 5)}
# () 튜플도 있다. 길이는  0
# (1,) 튜플도 있다. 길이는  1




###################################
# 4. 2차원 리스트에서 컴프리헨션 응용
#    모든 행에 대해 특정 열들만 뽑아내기.
print("< 4. 이차원 리스트에서 컴프리헨션 응용 -> 2d 리스트에서 특정 열들만 뽑아내기 >")
Map = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       [10, 11, 12]]

print("원본 Map 출력")
print(Map)
print()

# 만약 0, 2번 인덱스 컬럼만 추출하고싶음 -> 보통 조합으로 뽑아서 튜플로 지정함.
for combi in list(combinations([i for i in range(3)], 2)):
    cur = [[] for _ in range(len(Map))] # 행 만큼 준비
    for r in range(len(Map)):
        # cur[r].append(Map[r][col] for col in combi) #### 1 -> 안되는 이유???
        for col in combi:                             #### 2
            cur[r].append(Map[r][col])                #### 2

        # 열 정보를 넣어줄 때 위처럼 리스트 컴프리헨션을 통해 튜플의 모든 원소들을 열로하는 데이터를 집어넣을 수 있다.
    print("조합 ", combi, "에 대한 데이터를 cur[r].append(Map[r][col] for col in combi) 추출")
    print(cur)

print()
print()



###################################
# 5. 부분집합인지 판별 -> issubset
print("< 5. 집합1이 집합2의 부분집합인지 확인 -> 집합1.issubset(집합2) >")
setA = set([1, 2, 3])
setB = set([2])

print("setA는", setA, "입니다.")
print("setB는", setB, "입니다.")
if setB.issubset(setA):
    print(setB, "는 ", setA, "의 부분집합 입니다.")
    print("조건식은 if setB.issubset(setA): 입니다.")
print()
print()


####################################
# 6. 리스트 컴프리헨션 추가정리
print("< 6. 리스트 컴프리헨션 추가 정리 -> 재료 리스트가 있을 때/없을 때 >")
exists = [i for i in range(10)]
list1 = [x for x in range(10) if x % 2 == 0] # 리스트가 없을 때
list2 = [x if x % 2 == 0 else -1 for x in range(10)]

list3 = [x if x % 2 == 0 else -1 for x in exists]
list4 = [x for x in exists if x % 2 == 0]

print("리스트 준비 안되었을 때", list1)
print("리스트 준비 안되었을 때", list2)

print("리스트 준비 되었을 때", list3)
print("리스트 준비 되었을 때", list4)
myList = ['O']
print()
print()
####################################
# 7. 재귀 횟수 제한 증가
print("< 7. 재귀 횟수제한 증가 - sys.setrecursionlimit >")
print("import sys 후, sys.setrecursionlimit(횟수)")
import sys
sys.setrecursionlimit(10**6)

print()
print()
####################################
# 8. filter - https://wikidocs.net/22803
# map은 두 번째 iterable 인자들에 첫 번째 함수인자를 적용시킴
# filter은 주로 lambda함수를 활용해 특정 조건의 두 번째 iterable 인자의 원소들을 골라냄.

print("< 8. filter 함수 - iterable 변수에서 특정 조건의 원소들을 골라낼 때 사용한다. >")
print("target = [1, 2, 3, 4, 5, 6, 7, 8]")
print("filtered = list(filter(lambda x: x % 2 == 0, target))")
print("[2, 4, 6, 8]")

target = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = list(filter(lambda x: x % 2 == 0, target))
print(filtered) # [2, 4, 6, 8]

