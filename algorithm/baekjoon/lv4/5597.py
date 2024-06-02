"""
https://www.acmicpc.net/problem/5597
"""
import sys
interger_list = [val + 1 for val in range(30)]
for _ in range(28):
    target_interger = int(sys.stdin.readline().rstrip())
    interger_list.remove(target_interger)

interger_list = list(map(int,interger_list))
print(min(interger_list))
print(max(interger_list))