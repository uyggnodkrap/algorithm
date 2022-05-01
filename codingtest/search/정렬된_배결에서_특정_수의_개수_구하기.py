import sys
import bisect
N, x = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))
answer = bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)

if answer == 0:
    print(-1)
else:
    print(answer)
