"""
2016년
https://programmers.co.kr/learn/courses/30/lessons/12901
"""
import datetime

def solution(a, b):
    day = {0: "MON", 1: "TUE", 2: "WED", 3: "THU", 4: "FRI", 5: "SAT", 6: "SUN"}

    x = datetime.date(2016, a, b)
    print(x.weekday())
    return day[x.weekday()]