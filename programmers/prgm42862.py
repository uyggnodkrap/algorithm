"""
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
"""


def solution(n, lost, reserve):
    r = list(set(reserve) - set(lost))
    l = list(set(lost) - set(reserve))

    answer = n - len(l)

    for i in l:
        if i - 1 in r:
            answer += 1
            del r[r.index(i - 1)]

        elif i + 1 in r:
            answer += 1
            del r[r.index(i + 1)]

    return answer
