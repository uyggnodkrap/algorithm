"""
실패율
https://programmers.co.kr/learn/courses/30/lessons/42889
"""


def solution(N, stages):
    answer = []
    fail = []

    info = [0] * (N + 2)  # 각 단계 리스트
    for s in stages:
        info[s] += 1

    for i in range(1, N + 1):
        this_level = info[i]
        next_level = sum(info[i:])

        if next_level == 0:
            answer.append([0, i])
        else:
            answer.append([this_level / next_level, i])

    answer.sort(key=lambda x: (-x[0], x[1]))
    return [a[1] for a in answer]
