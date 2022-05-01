<<<<<<< HEAD
"""
카드 정렬하기
https://www.acmicpc.net/problem/1715
"""

import sys
import heapq


cards = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    cards.append(int(sys.stdin.readline().rstrip()))

heapq.heapify(cards)

if N == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        m1 = heapq.heappop(cards)
        m2 = heapq.heappop(cards)
        shuffle = m1+m2
        answer += shuffle
        heapq.heappush(cards, shuffle)

    print(answer)
=======
"""
카드 정렬하기
https://www.acmicpc.net/problem/1715
"""

import sys
import heapq


cards = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    cards.append(int(sys.stdin.readline().rstrip()))

heapq.heapify(cards)

if N == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        m1 = heapq.heappop(cards)
        m2 = heapq.heappop(cards)
        shuffle = m1+m2
        answer += shuffle
        heapq.heappush(cards, shuffle)

    print(answer)






>>>>>>> 22eb951 (intialization)
