"""
공유기 설치
https://www.acmicpc.net/problem/2110
"""

import sys

N, C = map(int, sys.stdin.readline().rstrip().split(' '))
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()
print(house)
