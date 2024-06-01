"""
https://www.acmicpc.net/problem/25304
"""
X = int(input())
N = int(input())
sum = 0
count = 0
while True:
    a, b = input().split()
    a, b = int(a), int(b)
    sum += a * b
    
    count += 1

    if N == count:
        break

print("Yes" if X == sum else "No")