"""
하샤드 수
https://programmers.co.kr/learn/courses/30/lessons/12947
"""

solution = lambda x : True if x % sum([int(i) for i in str(x)]) == 0 else False