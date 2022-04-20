"""
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584
"""
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        sec = 0
        price = prices.popleft()
        for p in prices:
            sec += 1
            if price > p:
                break
        answer.append(sec)

    return answer
