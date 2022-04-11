# """
# 빗물
# https://www.acmicpc.net/problem/14719
# """
#
a, b = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

answer = 0


def try1():
    tmp = arr[0]
    global answer
    for i in range(1, b-1):
        if tmp > arr[i]:
            print(tmp, arr[i], tmp - arr[i])
            answer += tmp - arr[i]
        else:
            tmp = max(arr[i+1:])

def try2():
    global answer
    for i in range(1, b-1):
        l = max(arr[:i])
        r = max(arr[i+1:])

        m = min(l, r)
        if m > arr[i]:
            answer += m - arr[i]

try2()
print(answer)