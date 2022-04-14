"""
예산
https://programmers.co.kr/learn/courses/30/lessons/12982
"""
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in range(len(d)):
        if d[i] <= budget:
            budget -= d[i]
            cnt += 1
            print(d[i], budget)
            if budget < 0:
                break
    return cnt
