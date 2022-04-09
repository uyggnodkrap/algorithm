# """
# N번째 큰 수
# https://www.acmicpc.net/problem/2693
# """
#
for _ in range(int(input())):
    x = list(map(int, input().split(' ')))
    x.sort()
    print(x[-3])
