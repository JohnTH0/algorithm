"""
https://www.acmicpc.net/problem/10871
"""
import sys
N_X = sys.stdin.readline().rstrip().split()
X = int(N_X[1])
interger_list = sys.stdin.readline().rstrip().split()
result_string = ""
for int_val in interger_list:
    int_val = int(int_val)
    if int_val < X:
        result_string += "{} ".format(int_val)
print(result_string)