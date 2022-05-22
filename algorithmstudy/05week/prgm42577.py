"""
전화번호 목록
https://programmers.co.kr/learn/courses/30/lessons/42577
"""

"""
def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[j].startswith(phone_book[i]):
                answer = False
                break
    
    return answer
"""

"""

from itertools import combinations
def solution(phone_book):
    answer = True
    phone_book.sort(key = lambda x : len(x))
    comb_phone_book = combinations(phone_book, 2)
    for c in comb_phone_book:
        if c[1].startswith(c[0]):
            answer = False
            break
    
    return answer
"""

def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True