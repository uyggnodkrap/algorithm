import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
answer = -1

start = 0
end = N - 1
answer = -1
while start <= end:
    mid = (start + end) // 2

    if arr[mid] == mid:
        answer = mid
        break

    elif arr[mid] < mid:
        start = mid + 1

    else:
        end = mid - 1

print(answer)
