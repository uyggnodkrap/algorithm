"""
프린터
https://programmers.co.kr/learn/courses/30/lessons/42587
"""

from collections import deque

def solution(priorities, location):
    prior = deque([[priorities[i], i] for i in range(len(priorities))])
    answer = []
    idx = 1
    
    while prior:
        max_prior = max(prior)
        p = prior.popleft()
        
        if p[0] == max_prior[0]:
            answer.append(p[1])
        else:
            prior.append(p)
            
    return answer.index(location)+1