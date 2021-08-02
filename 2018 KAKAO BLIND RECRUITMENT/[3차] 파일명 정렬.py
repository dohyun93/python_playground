# https://programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    splited = [re.split(r"([0-9]+)", s) for s in files]
    sort = sorted(splited, key=lambda x: (x[0].lower(), int(x[1])))
    return ["".join(s) for s in sort]

result = solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
print(result)

# 문자열 옵션으로 주면 이 내용으로 모두 합쳐 문자열로 만듬.
# 14라인에서 각 리스트의 요소들이 리스트 이므로 이를 옵션으로 줘서 문자열로 다시 조합.
myList = ['a', 'b', 'c', 'd']
answer = ''.join(myList)
print(answer)