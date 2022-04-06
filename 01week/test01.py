"""
https://programmers.co.kr/learn/courses/30/lessons/12906
"""

from collections import deque

def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]

    while arr:
        x = arr.popleft()
        if answer[-1] != x:
            answer.append(x)

    return answer