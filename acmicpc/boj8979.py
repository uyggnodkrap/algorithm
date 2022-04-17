"""
올림픽
https://www.acmicpc.net/problem/8979
"""
import sys

n, k = map(int, sys.stdin.readline().split(' '))

participants = []
for i in range(n):
    participants.append(list(map(int, sys.stdin.readline().split(' '))))
participants.sort(key = lambda x: (x[1], x[2], x[3]))
participants = participants[::-1]
idx = 0
for i in range(n):
    if participants[i][0] == k:
       idx = i

for i in range(n):
    if participants[i][1:] == participants[idx][1:]:
        print(i+1)
        break

