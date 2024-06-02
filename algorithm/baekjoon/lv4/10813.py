"""
https://www.acmicpc.net/problem/10813
"""

import sys
N_M = sys.stdin.readline().rstrip().split()
N = int(N_M[0])
M = int(N_M[1])
interger_list = [val + 1 for val in range(N)]
for _ in range(M):
    i_j = sys.stdin.readline().rstrip().split()
    i = int(i_j[0])
    j = int(i_j[1])
    interger_list[i-1], interger_list[j-1] = interger_list[j-1], interger_list[i-1]

result_string = " ".join(map(str, interger_list))
print(result_string)