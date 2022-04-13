"""
모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
"""


def correct(arr1, arr2):
    cnt = 0
    for a, b in zip(arr1, arr2):
        if a == b:
            cnt+= 1
    return cnt

def solution(answers):
    answer = []
    s1 = ([1, 2, 3, 4, 5] * 2000)[:len(answers)]
    s2 = ([2, 1, 2, 3, 2, 4, 2, 5] * 1250)[:len(answers)]
    s3 = ([3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000)[:len(answers)]
    cor = []
    cor.append(correct(s1, answers))
    cor.append(correct(s2, answers))
    cor.append(correct(s3, answers))
    m = max(cor)
    for i in range(len(cor)):
        if cor[i] == m:
            answer.append(i+1)

    return answer