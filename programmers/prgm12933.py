"""
정수 내림차순으로 배치하기
https://programmers.co.kr/learn/courses/30/lessons/12933
"""
def solution(n):
    n = int(n)
    n = [i for i in str(n)]
    n.sort(reverse=True)
    return int(''.join(n))