# https://programmers.co.kr/learn/courses/30/lessons/42892

import sys

sys.setrecursionlimit(10 ** 6)

class Tree:
    def __init__(self, nodes):
        self.Root = max(nodes, key=lambda x: x[1])
        leftList = list(filter(lambda x: x[0] < self.Root[0], nodes))
        rightList = list(filter(lambda x: x[0] > self.Root[0], nodes))

        if leftList == []:
            self.left = None
        else:
            self.left = Tree(leftList)

        if rightList == []:
            self.right = None
        else:
            self.right = Tree(rightList)

def make(node, preList, postList):
    preList.append(node.Root)
    if node.left is not None:
        make(node.left, preList, postList)
    if node.right is not None:
        make(node.right, preList, postList)
    postList.append(node.Root)

def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []
    make(root, postList, preList)
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, preList)))
    answer.append(list(map(lambda x: nodeinfo.index(x) + 1, postList)))
    return answer

dataList = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
data = max(dataList,key=lambda x :x[1])
print(data)