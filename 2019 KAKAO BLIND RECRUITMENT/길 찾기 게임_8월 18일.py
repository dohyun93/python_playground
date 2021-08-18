# https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
sys.setrecursionlimit(10**6)
class Tree:
    def __init__(self,dataList):
        self.data=max(dataList,key=lambda x :x[1])
        leftList =list(filter(lambda x :x[0] < self.data[0] , dataList))
        rightList = list(filter(lambda x :x[0] > self.data[0] , dataList))
        if leftList != []:
            self.left=Tree(leftList)
        else :
            self.left=None
        if rightList != []:
            self.right=Tree(rightList)
        else :
            self.right=None

def fix(node,postList,preList):
    postList.append(node.data)
    if node.left is not None:
        fix(node.left,postList,preList)
    if node.right is not None:
        fix(node.right,postList,preList)
    preList.append(node.data)

def solution(nodeinfo):
    answer = []
    root = Tree(nodeinfo)
    postList = []
    preList = []
    fix(root,postList,preList)
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,postList)))
    answer.append(list(map(lambda x: nodeinfo.index(x)+1 ,preList)))
    return answer