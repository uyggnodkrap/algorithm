"""
피보나치 수열
"""

# 재귀 방식
def fibo_recursive(x):
    print("f({})".format(x), end = ' ')
    if x in (1, 2):
        return 1
    else:
        return fibo_recursive(x-1) + fibo_recursive(x-2)

print(fibo_recursive(10))

# dp 방식 
def fibo_dp(x):
    dp = [0, 1, 1]
    for i in range(3, x+1):
        print("f({})".format(i), end = ' ')
        dp.append(dp[i-1] + dp[i-2])
    return dp[-1]

print(fibo_dp(10))
