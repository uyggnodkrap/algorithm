"""
[3차] 압축
https://programmers.co.kr/learn/courses/30/lessons/17684
"""

from collections import deque
def solution(msg):
    answer = []
    alphabet = {chr(65+i): i+1 for i in range(26)}
    msg = deque(msg)
    value = 26
    word = ""
    
    while len(msg) != 1:
        word += msg.popleft()
        v1 = alphabet[word]
        v2 = alphabet[msg[0]]
        
        if word+msg[0] not in alphabet.keys():
            value += 1
            alphabet[word+msg[0]] = value
            answer.append(v1)
            word = ""
        
    answer.append(alphabet[word+msg[0]])
        
    return answer