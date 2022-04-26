import sys

arr = []
for _ in range(int(sys.stdin.readline())):
    arr.append(int(sys.stdin.readline()))

arr.sort(reverse=True)
for a in arr:
    print(a, end=' ')