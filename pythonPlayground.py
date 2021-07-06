# $$$ 수 입력
import sys
from itertools import permutations, combinations, product, combinations_with_replacement # -> 순열, 조합, 중복허용 순열/조합
from bisect import bisect_left, bisect_right # 정렬된 iterable에서 이진탐색 인덱스 활용 -> bisect_left(list, 숫자)
from collections import deque, Counter # 왼쪽 오른쪽 삽입 가능한 deque (인덱싱은 안됨), 횟수 카운팅해주는 것
import heapq # 힙 -> 최단경로문제 자주활용. heapq.heappush(리스트, 요소), heapq.heappop(리스트)
import math
# sys.stdin.readline().rstrip()
# 또는 한 개는 int(input())
# 또는 여러개는 m, n = map(int, input().split())

# $$$ 숫자 기본.
num1 = 10
num2 = 3

print(num1 / num2) # 계산결과 자체 (소수부포함)
print(num1 // num2)# 몫
print(num1 % num2) # 나머지
print(num1 ** num2)# 거듭제곱
print(round(num1/num2, 2)) # num1/num2 결과를 셋째 자리에서 반올림.
print(round(num1/num2)) # 별다른 인자전달없으면 소수점 첫째 자리에서 반올림.

# $$$ 리스트 컴프리헨션
List1 = [i for i in range(10)]
print(List1)
excludeList = [2, 4, 6, 8]
excluded = [i for i in List1 if i not in excludeList] # 미리생성된 리스트 요소없는 것으로 생성
print(excluded)
List2 = [i for i in range(10) if i % 2 != 0] # 조건주고 해당원소 안넣고 리스트 초기화
print(List2)

# $$$ string
string1 = '"나의 작은 \'라임 오렌지 나무" 입니다.'
string2 = "너는 누구냐라는 '엄마'에게 나는 \" 라고했다."
print(string1)
print(string2)

# $$$ list, tuple, dict, set
_list = [1, 2, 3]
_tuple = (1, 2, 3) # 값 변경 불가하므로, 서로다른 성격의 데이터를 활용할 때 + 최단경로 문제에서 주로 사용. ((노드1, 비용1), ...)
_dict = {"name": "권도현", "나이": 29, "원징": 5700}
_set = {1, 2, 3} # 중복 값 불가. dict과 마찬가지로 non-iterable 자료형임.
key_list = _dict.keys()
value_list = _dict.values()
print(key_list, value_list)
print(list(key_list), list(value_list))
for key in key_list: # .keys()로 한 dict_keys 타입으로 순회 가능하다.
    print(_dict[key])
# set의 연산은: |, &, - 로 OR, AND, 차집합 이다.
# 추가로 add, remove, update가 있는데,
_set.add(4) # 값 한 개 추가
print(_set)
_set.remove(2) # 값 한 개 제거
print(_set)
_set.update([5, 6, 7]) # 값 여러개 추가.
print(_set)

for i in _dict: # 이렇게해도 dict 키 가져옴.!!!!!
    print(i)
    print(_dict[i])

# 1. 'in' grammar.
# in -> iterable 자료형(문자열, 리스트, 튜플) 뿐 아니라, dict, set도 가능.

mySet = {1, 2, 3}
for i in mySet:
    print(i)

mydict = {"age": 29, "name": "kwondohyun"}
for key in mydict:
    print(mydict[key])

print((lambda a, b: a+b)(39999999, 4))

# mynum = int(input())
# print(mynum)
# r, c = map(int, input().split())
# print(r, c)
#
# array2D = [[0]*c for _ in range(r)]
# print(array2D)
# array2D[2][1] = 7
# print(array2D)

myList = [1, 2, 3, 4, 5]
print(min(mySet))
print(max(mySet))


# r, c = map(int, input().split())
# myMap = [[0]*c for _ in range(r)]
# print(myMap)
# for i in range(r):
#     data = list(map(int, sys.stdin.readline().rsplit()))
#     myMap[i] = data
#
# print(myMap)
#
# print(f"행과 열은 {r}, {c} 입니다.")

######################## 기타 패키지 및 라이브러리 ##############
# 1. itertools -> 순열과 조합
myData = ['A', 'B', 'C']
permu = list(permutations(myData, 3)) # myData에서 3개를 뽑아 만들 수 있는 순열.
print(permu)
combi = list(combinations(myData, 2)) # myData에서 2개를 뽑아 만들 수 있는 조합.
print("fuck", combi)
permu_repeat = list(product(myData, repeat=2)) # myData에서 2개를 중복 허용해서 만들 수 있는 수열.
print(permu_repeat)
combi_repl = list(combinations_with_replacement(myData, 2)) # myData에서 2개를 중복 허용해서 만들 수 있는 조합
print(combi_repl)

###################  heapq ####################
# heapq.heappush / heapq.heappop -> O(nlogn)소요.
# dijkstra 알고리즘 구현 뿐 아니라 최단경로 문제를 풀 때 사용.
# 우선순위 큐 기능을 구현하고자 할 때 사용한다.
# 힙 소트

data = [9, 2, 398, 19, 22, -1, -332, -234, 298, 12]

def heapsort(data):
    h = []
    result = []
    for i in data:
        heapq.heappush(h, i)
        # heapq.heappush(h, -i)

    for i in range(len(h)):
        result.append(heapq.heappop(h))
        # result.append(-heapq.heappop(h))

    return result

sorted = heapsort(data)
print(sorted)

#################  bisect ##################

leftidx = bisect_left(sorted, 10) # 주어진 정렬된 iteralbe 자료형에서 데이터를 삽입할 가장 왼쪽 인덱스
rightidx = bisect_right(sorted, 92) # 주어진 정렬된 iteralbe 자료형에서 데이터를 삽입할 가장 오른쪽 인덱스
print(leftidx, rightidx)

############### collections ################
# dq = deque()
# dq.appendleft(val) / dq.append(val) / dq.popleft() / dq.pop()
# deque는 인덱싱 불가.

data = deque()
data.appendleft(0)
leftdata = data.popleft()

counter = Counter(['red', 'yellow', 'green', 'green', 'blue', 'blue'])
print(counter['red']) # 1
print(counter['green'])  # 2

################ math ##################
a, b = 12, 3
print(math.e)
print(math.pi)
print(math.gcd(a, b))
print(a*b/math.gcd(a, b))
print(math.sqrt(a))
print(math.factorial(b))