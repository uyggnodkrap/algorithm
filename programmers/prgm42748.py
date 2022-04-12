"""
K번째수
https://programmers.co.kr/learn/courses/30/lessons/42748
"""


def solution(array, commands):
    answer = []

    for command in commands:
        an = array[command[0] - 1:command[1]]
        an.sort()
        answer.append(an[command[2] - 1])
    return answer