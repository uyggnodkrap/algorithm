import sys

# M: 세로, N: 가로
M, N, K = map(int, sys.stdin.readline().split(' '))

area = [["O"] * N] * M

# print(area[2][6])
for a in area:
    print(a)

for _ in range(K):
    x = list(map(int, sys.stdin.readline().split(' ')))
    x1 = x[:2]
    x2 = x[2:]

    # x1[0] = N -1 - x1[0]
    x1[1] = M - x1[1]

    # x2[0] = N -1 - x2[0]
    x2[1] = M - x2[1]

    for i in range(x2[1], x1[0]):
        for j in range(x1[0], x[2]):
            print(i, j)
        print()

    print(x1, x2)

