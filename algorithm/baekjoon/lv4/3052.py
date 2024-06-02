"""
https://www.acmicpc.net/problem/3052
"""
import sys

result_list = []
for _ in range(10):
    input_integer = int(sys.stdin.readline().rstrip())
    result_list.append(input_integer%42)

result_list = set(result_list)
print(len(result_list))