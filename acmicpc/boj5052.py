"""
전화번호 목록
https://www.acmicpc.net/problem/5052
"""

import sys
input = sys.stdin.readline

for _ in range(int(sys.stdin.readline().rstrip())):
    arr = []
    answer = "YES"

    for _ in range(int(sys.stdin.readline().rstrip())):
        arr.append(sys.stdin.readline().rstrip())

    arr.sort()

    for a, b in zip(arr, arr[1:]):
        if b.startswith(a):
            answer = "NO"
            break

    print(answer)
