"""
일곱 난쟁이
https://www.acmicpc.net/problem/2309
"""
import sys
from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(sys.stdin.readline().rstrip()))

arr_x = combinations(arr, 7)

for a in arr_x:
    if sum(a) == 100:
        answer = list(a)
        answer.sort()
        for an in answer:
            print(an)
        break
