"""
전자레인지
https://www.acmicpc.net/problem/10162
"""

import sys

t = int(sys.stdin.readline().rstrip())

if t % 10 != 0:
    print(-1)
else:
    answer = []
    a, b = divmod(t, 300)
    answer.append(a)
    t = b

    a, b = divmod(t, 60)
    answer.append(a)
    t = b

    a, b = divmod(t, 10)
    answer.append(a)
    t = b

    for i in answer:
        print(i)