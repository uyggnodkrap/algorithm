"""
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/12921
"""
def solution(x):
    arr = [False, False] + [True] * (x-1)
    for i in range(2, x+1):
        if arr[i]:
            for j in range(i*2, x+1, i):
                arr[j] = False
    return len([k for k in arr if k == True])