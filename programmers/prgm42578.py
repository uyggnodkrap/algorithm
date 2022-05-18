"""
위장
https://programmers.co.kr/learn/courses/30/lessons/42578
"""

def solution(clothes):
    answer = 1
    clothes_dict = {}
    for c in clothes:
        if c[1] not in clothes_dict:
            clothes_dict[c[1]] = 1
        else:
            clothes_dict[c[1]] += 1
    
    
    for k, v in clothes_dict.items():
        
        answer *= (v+1)
    
    return answer - 1