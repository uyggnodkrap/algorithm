# """
# 빗물
# https://www.acmicpc.net/problem/14719
# """
#
a, b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

answer = 0

for i in range(1, b-1):
    l = max(arr[:i])
    r = max(arr[i+1:])

    m = min(l, r)
    if m > arr[i]:
        answer += m - arr[i]

print(answer)