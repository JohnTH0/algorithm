"""
https://www.acmicpc.net/problem/10811
"""
import sys

N_M = sys.stdin.readline().rstrip().split()
N = int(N_M[0])
M = int(N_M[1])

integer_list = list(map(int,[val + 1 for val in range(N)]))

for _ in range(M):
    i_j = sys.stdin.readline().rstrip().split()
    i = int(i_j[0])
    j = int(i_j[1])
    integer_list[i-1:j] = integer_list[i-1:j][::-1]

print(" ".join(map(str,integer_list)))