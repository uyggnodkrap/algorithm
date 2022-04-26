import sys

N = int(sys.stdin.readline().rstrip())
store = sorted(map(int, sys.stdin.readline().rstrip().split(' ')))
M = int(sys.stdin.readline().rstrip())
customer = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# solution1 이진 탐색
def binary_search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2

        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            return "yes"

    return "no"


for c in customer:
    print(binary_search(store, c, 0, N), end=" ")
