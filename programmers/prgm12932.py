"""
자연수 뒤집어 배열로 만들기
https://programmers.co.kr/learn/courses/30/lessons/12932
"""
solution = lambda n: [int(i) for i in str(n)][::-1]