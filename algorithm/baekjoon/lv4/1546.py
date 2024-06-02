"""
https://www.acmicpc.net/problem/1546
"""

import sys
N = int(sys.stdin.readline().rstrip())
score_string = sys.stdin.readline().rstrip().split()
integer_list = list(map(int,score_string))
result_list = []
M = max(integer_list)

for score in integer_list:
    result_list.append(score/M*100)

print(sum(result_list)/N)
