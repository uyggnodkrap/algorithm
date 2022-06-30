"""
숫자 카드 -> 제출 아직 안함
https://www.acmicpc.net/problem/10815
"""

import sys
import bisect

n = int(sys.stdin.readline().rstrip())
card = list(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split(' ')))

answer = []

for i in range(m):
    t = bisect.bisect_right(card, numbers[i])
    if  t!= 0:
        print(1)
    else:
        print(0)
