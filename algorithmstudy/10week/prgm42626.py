"""
더 맵게
https://programmers.co.kr/learn/courses/30/lessons/42626
"""

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            break
        elif not scoville:
            answer = -1
            break
        else:
            min2 = heapq.heappop(scoville)
            heapq.heappush(scoville, min1 + min2*2)
            answer += 1
    
    return answer