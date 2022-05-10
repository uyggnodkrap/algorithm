"""
진법변환/비트연산
"""

# 1. 진법 변환
x = 153
# 10진법 -> 2진법
binx = bin(x)
print(binx)

# 10진법 -> 8진법
octx = oct(x)
print(octx)

# 10진법 -> 16진법
hexx = hex(x)
print(hexx)

# n진법 -> 10진법

print(int(binx, 2))
print(int(octx, 8))
print(int(hexx, 16))

# 2. 비트연산
# 1. and
# 각각의 자릿수를 비교하여 둘 다 1이면 1, 그렇지 않으면 0 

# 2. or
# 각각의 자릿수를 비교하여 둘 다 0이면 0, 그렇지 않으면 1

# 3. xor
# 각각의 자릿수가 서로 같음 0, 다르면 1 
# 4. not 
# 2의 보수가 적용된 음수로 만들음
# 5. shift
# >: 나누기, <: 곱하기