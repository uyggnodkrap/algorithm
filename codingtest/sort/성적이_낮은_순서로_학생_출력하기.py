import sys

student = []
for _ in range(int(sys.stdin.readline())):
    student.append(list(sys.stdin.readline()[:-1].split(' ')))

student.sort(key=lambda x: int(x[1]))

for s in student:
    print(s[0], end=' ')
