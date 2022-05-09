"""
팩토리얼 진법
https://www.acmicpc.net/problem/5692
"""

import sys


fact = [0, 1]
for i in range(2, 6):
    fact.append(i*fact[i-1])

while True:
    x = sys.stdin.readline().rstrip()
    answer = 0

    if x == "0":
        break
    else:
        x = x[::-1]
        for i in range(len(x)):
            answer += fact[i+1] * int(x[i])

    print(answer)

    