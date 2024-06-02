"""
https://www.acmicpc.net/problem/10818
"""
import sys
N = sys.stdin.readline()
integer_list = list(map(int,sys.stdin.readline().rstrip().split()))
print("{} {}".format(min(integer_list), max(integer_list)))