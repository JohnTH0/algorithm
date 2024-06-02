"""
https://www.acmicpc.net/problem/2562
"""

import sys

interger_list = []
for _ in range(9):
    input_integer = int(sys.stdin.readline().rstrip())
    interger_list.append(input_integer)

max_integer = max(interger_list) 
print(max_integer)
print(interger_list.index(max_integer) + 1)
