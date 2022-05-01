<<<<<<< HEAD
"""
안테나
https://www.acmicpc.net/problem/18310
"""
import sys
N = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split(' ')))

house.sort()
print(house[(N-1)//2])
=======
"""
안테나
https://www.acmicpc.net/problem/18310
"""
import sys
N = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split(' ')))

house.sort()
print(house[(N-1)//2])
>>>>>>> 22eb951 (intialization)
