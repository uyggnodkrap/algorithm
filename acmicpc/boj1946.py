"""
신입 사원
https://www.acmicpc.net/problem/1946
"""

import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    arr = []
    n = int(sys.stdin.readline().rstrip())

    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split(' '))
        arr.append([a, b])

    arr.sort(key = lambda x: x[0])
    interview_score = arr[0][1]
    hired = 1
    
    for i in range(1, n):
        if arr[i][1] < interview_score:
            hired += 1
            interview_score = arr[i][1]

    print(hired)
