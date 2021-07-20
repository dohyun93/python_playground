# 트라이 알고리즘은 문자열을 효율적으로 검색하기 위해 사용되는 자료구조로,
# 자동완성이나 검색어 추천 기능에서 주로 사용되는 알고리즘이다.
#
# 이진탐색의 경우 숫자는 O(logN)으로 검색이 가능하지만, 최대 M 길이의 문자열들이 N개 있다면
# O(MlogN)의 시간복잡도가 소요될 것이다.
#
# 트라이 알고리즘은 트리 형태의 자료구조와 flag를 이용해 O(M)만에 문자열 탐색이 가능하다.
# 15-4 가사 검색이라는 카카오 문자열 문제에 대해 솔루션 구현에 사용되며 문자열 관련 회사니 핵심 유형이다.

class Node(object):
    def __init__(self, key, data=None):
        self.key = key # 값으로 입력될 문자.
        self.data = data # 문자열의 종료를 알리는 flag
        self.children = {} # 자식 노드를 저장하는 사전 자료형

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            # 자식노드 없으면 추가
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            # 현재 노드를 char에 대한 자식노드로 이동
            current_node = current_node.children[char]
        # 노드의 데이터 멤버변수에 입력한 string 할당.
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                # 현재 문자가 자식노드에 있다면
                current_node = current_node.children[char]
            else:
                return False
        
        if current_node.data:
            return True
        else:
            return False
    
    # prefix 로 시작하는 문자열 찾기
    def starts_with(self, prefix):
        current_node = self.head
        words = []

        # prefix에 해당하는 노드까지 내려가기
        for p in prefix:
            if p in current_node.children:
                current_node = current_node.children[p]
            else:
                return None
        
        # prefix 이후 단어들 찾기
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                # flag인 노드라면 prefix에 해당되는 단어를 모음.
                if node.data:
                    words.append(node.data)
                # 그 다음 탐색할 노드들에 자식 노드들 추가. (키(문자)값에 대한 밸류(노드) 리스트 extend.)
                next_node.extend(list(node.children.values()))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return words

trie = Trie()
word_list = ["Choonsik", "Ryan", "Frodo"]
for word in word_list:
    trie.insert(word)

print("춘식이가 있나?", trie.search("Choonsik"))
print("춘 으로 시작하는 단어가 있나?", trie.starts_with("Choon"))