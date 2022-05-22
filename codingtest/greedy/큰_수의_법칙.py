"""
큰 수의 법칙
"""
def solution1(x, m, k):
    answer = 0
    x.sort()
    max1 = x[-1]
    max2 = x[-2]
    for i in range(1, m+1):
        if k%i != 0:
            answer += max1
        else:
            answer += max2

    return answer

def solution2(x, m, k):
    x.sort()
    max1 = x[-1]
    max2 = x[-2]
    a, b = divmod(m,k+1)
    cnt = (a*k)+b
    answer = max1 * cnt + max2*(m-cnt)
    return answer

import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split(' '))
arr = list(map(int, sys.stdin.readline().rstrip().split(' ')))

print(solution1(arr, m, k))
print(solution2(arr, m, k))
