import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def solution1(M, arr):
    mini = min(arr)
    x = [M+1]
    while sum(x) > M:
        mini += 1
        x = [a - mini if a > mini else 0 for a in arr]

    print(max(arr) - max(x))


def solution2(M, arr):
    start = 0
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2
        total = sum([a - mid if a - mid > 0 else 0 for a in arr])

        if total < M:
            end = mid -1
        else:
            result = mid
            start = mid + 1

    print(result)


solution1(M, arr)
solution2(M, arr)


