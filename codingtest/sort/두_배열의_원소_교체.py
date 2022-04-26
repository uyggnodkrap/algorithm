import sys
N, K = map(int, sys.stdin.readline().split(' '))

arr1 = list(map(int, sys.stdin.readline().split(' ')))
arr2 = list(map(int, sys.stdin.readline().split(' ')))

arr1.sort()
arr2.sort(reverse=True)

answer = sum(arr1)
for i in range(K):
    answer -= arr1[i]
    answer += arr2[i]

print(answer)
