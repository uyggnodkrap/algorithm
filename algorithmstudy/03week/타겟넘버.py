
"""
타겟 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
"""


# 풀이 1. 완전탐색

def brute_force(n, t):
    from itertools import product
    l = [(x, -x) for x in n]
    s = list(map(sum, product(*l)))
    return s.count(t)


# 풀이 2. bfs

def bfs(num, target):
    node = [0]
    for i in num:
        leaf = []
        for n in node:
            leaf.append(n+i)
            leaf.append(n-i)
        node = leaf
    return node.count(target)



def solution(numbers, target):
    answer1 = brute_force(numbers, target)
    answer2 = bfs(numbers, target)
    return answer1
