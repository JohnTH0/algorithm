"""
https://www.acmicpc.net/problem/2588
"""
x = input()
y = input()

x = int(x)
y1 = y[2]
y2 = y[1]
y3 = y[0]
y = int(y)
print(x * int(y1))
print(x * int(y2))
print(x * int(y3))
print(x * y)