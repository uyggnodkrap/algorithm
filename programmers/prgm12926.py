"""
시저 암호
https://programmers.co.kr/learn/courses/30/lessons/12926
"""

def solution(s, n):
    answer = ''

    large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    small = large.lower()

    for i in s:
        if i in large:
            answer += large[large.index(i) + n]
        elif i in small:
            answer += small[small.index(i) + n]
        else:
            answer += ' '

    return answer
