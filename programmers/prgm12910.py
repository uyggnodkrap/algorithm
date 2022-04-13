"""
나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910
"""
def solution(arr, divisor):
    answer = [a for a in arr if a%divisor == 0]
    answer.sort()
    return answer if answer else [-1]