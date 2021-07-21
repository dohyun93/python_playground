# 효율성은 실패./
def solution(words, queries):
    result = []
    for query in queries:
        answer = 0
        length = len(query)
        if query[0] == "?": # ????abc
            suffix = query.split("?")[-1]
            for word in words:
                # query가 모두 ??? 로 이루어져있고 길이가 word와 동일하다면 무조건 일치.
                if len(word) == length and len(suffix) == 0:
                    answer += 1
                # query suffix로 끝나고 길이도 word와 query 가 동일한 경우 정답처리.
                elif len(word) == length and word.endswith(suffix):
                    answer += 1
        else:
            prefix = query.split("?")[0]
            for word in words:
                if len(word) == length and word.startswith(prefix):
                    answer += 1
                elif len(word) == length and len(prefix) == 0:
                    answer += 1
        result.append(answer)
    return result


# https://programmers.co.kr/learn/courses/30/lessons/60060
# 문제 설명
# [본 문제는 정확성과 효율성 테스트 각각 점수가 있는 문제입니다.]
#
# 친구들로부터 천재 프로그래머로 불리는 "프로도"는 음악을 하는 친구로부터 자신이 좋아하는 노래 가사에 사용된 단어들 중에 특정 키워드가 몇 개 포함되어 있는지 궁금하니 프로그램으로 개발해 달라는 제안을 받았습니다.
# 그 제안 사항 중, 키워드는 와일드카드 문자중 하나인 '?'가 포함된 패턴 형태의 문자열을 뜻합니다. 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정합니다. 예를 들어 "fro??"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않습니다.
#
# 가사에 사용된 모든 단어들이 담긴 배열 words와 찾고자 하는 키워드가 담긴 배열 queries가 주어질 때, 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 반환하도록 solution 함수를 완성해 주세요.
#
# 가사 단어 제한사항
# words의 길이(가사 단어의 개수)는 2 이상 100,000 이하입니다.
# 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 가사 단어 길이의 합은 2 이상 1,000,000 이하입니다.
# 가사에 동일 단어가 여러 번 나올 경우 중복을 제거하고 words에는 하나로만 제공됩니다.
# 각 가사 단어는 오직 알파벳 소문자로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드 제한사항
# queries의 길이(검색 키워드 개수)는 2 이상 100,000 이하입니다.
# 각 검색 키워드의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다.
# 전체 검색 키워드 길이의 합은 2 이상 1,000,000 이하입니다.
# 검색 키워드는 중복될 수도 있습니다.
# 각 검색 키워드는 오직 알파벳 소문자와 와일드카드 문자인 '?' 로만 구성되어 있으며, 특수문자나 숫자는 포함하지 않는 것으로 가정합니다.
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며, '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.
# 예를 들어 "??odo", "fro??", "?????"는 가능한 키워드입니다.
# 반면에 "frodo"('?'가 없음), "fr?do"('?'가 중간에 있음), "?ro??"('?'가 양쪽에 있음)는 불가능한 키워드입니다.

# 입출력 예
# words	queries	result
# ["frodo", "front", "frost", "frozen", "frame", "kakao"]	["fro??", "????o", "fr???", "fro???", "pro?"]	[3, 2, 4, 1, 0]
# 입출력 예에 대한 설명
# "fro??"는 "frodo", "front", "frost"에 매치되므로 3입니다.
# "????o"는 "frodo", "kakao"에 매치되므로 2입니다.
# "fr???"는 "frodo", "front", "frost", "frame"에 매치되므로 4입니다.
# "fro???"는 "frozen"에 매치되므로 1입니다.
# "pro?"는 매치되는 가사 단어가 없으므로 0 입니다.

# https://codingffler.tistory.com/24
class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        curNode = self.head

        for char in string:
            curNode.count += 1 # 현재노드를 거쳐 입력된 문자열 수
            if char not in curNode.children:
                curNode.children[char] = Node(char)

            curNode = curNode.children[char]

        curNode.count += 1 # 마지막 노드 도달 처리.

    def startswith(self, prefix):
        curNode = self.head
        result = 0
        for char in prefix:
            if char == "?":
                break

            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return 0

        return curNode.count # prefix로 시작하는 문자열 존재 개수 리턴.

def solution(words, queries):
    answer = []
    tries = {}
    reverse_tries = {}

    for word in words:
        if len(word) in tries:
            tries[len(word)].insert(word)
            reverse_tries[len(word)].insert(reversed(word))
        else:
            trie = Trie()
            reverse_trie = Trie()

            trie.insert(word)
            reverse_trie.insert(reversed(word))

            tries[len(word)] = trie
            reverse_tries[len(word)] = reverse_trie

    for query in queries:
        if len(query) in tries:
            if query[0] != "?":
                trie = tries[len(query)]
                answer.append(trie.startswith(query))
            else:
                trie = reverse_tries[len(query)]
                answer.append(trie.startswith(reversed(query)))
        else:
            answer.append(0)

    return answer

