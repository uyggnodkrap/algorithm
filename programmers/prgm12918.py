"""
문자열 다루기 기본
https://programmers.co.kr/learn/courses/30/lessons/12918
"""

def solution(s):
    if s.isdigit() and (len(s) == 4 or len(s) == 6):
        return True
    else:
        return False