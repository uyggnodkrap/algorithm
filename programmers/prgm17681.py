"""
[1차] 비밀지도
https://programmers.co.kr/learn/courses/30/lessons/17681
"""

def solution(n, arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        q = (bin(x | y))[2:]

        if len(q) < n:
            q = "0" * (n - len(q)) + q
        q = q.replace("1", "#").replace("0", " ")
        answer.append(q)

    return answer
