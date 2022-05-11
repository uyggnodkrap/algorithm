"""
소수 만들기
https://programmers.co.kr/learn/courses/30/lessons/12977
"""

from itertools import combinations
def solution(nums):
    answer = 0
    prime = [False, False] + [True] * (50000-1)
    for i in range(1, 50000+1):
        if prime[i]:
            for j in range(i+i, 50000+1, i):
                prime[j] = False
                
    arr = combinations(nums, 3)
    
    for a in arr:
        if prime[sum(a)]:
            answer+= 1

    return answer