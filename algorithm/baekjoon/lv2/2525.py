"""
https://www.acmicpc.net/problem/2525
"""

A, B  = input().split()
A, B = int(A), int(B)
C = int(input())

total_minute = (60 * A) + B + C
A = (total_minute // 60) % 24
B = total_minute % 60
print("{} {}".format(A, B))