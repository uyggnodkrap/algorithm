"""
국영수
https://www.acmicpc.net/problem/10825
"""

import sys

students = []
for _ in range(int(sys.stdin.readline().rstrip())):
    student = sys.stdin.readline().rstrip().split(' ')
    student[1:] = map(int, student[1:])
    students.append(student)

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])
