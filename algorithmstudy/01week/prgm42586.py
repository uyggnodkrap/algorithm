"""
기능개발
https://programmers.co.kr/learn/courses/30/lessons/42586
"""

import math


def solution(progresses, speeds):
    answer = []
    work = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]

    day = 1
    idx = 0

    for i in range(1, len(work)):
        if work[idx] >= work[i]:
            day += 1
        else:
            print(work[i], work[idx], i)
            answer.append(day)
            idx = i
            day = 1

    answer.append(day)
    return answer
