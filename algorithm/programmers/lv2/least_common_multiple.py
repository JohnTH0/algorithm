"""
최소공배수
https://school.programmers.co.kr/learn/courses/30/lessons/12953
lv 2
"""
import math
def solution(arr):
    lcm = 1
    for i in arr:
        lcm = lcm*i//math.gcd(lcm, i)

# python 3.9+
# def solution(arr):
#     return math.lcm(*arr)

arr = [2,6,8,14]
solution(arr)

