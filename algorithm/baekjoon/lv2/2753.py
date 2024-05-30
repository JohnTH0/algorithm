"""
https://www.acmicpc.net/problem/2753
"""
input_year = input()
input_year = int(input_year)

if input_year % 4 == 0 and input_year % 100 != 0:
    print(1)
elif input_year % 400 == 0:
    print(1)
else:
    print(0)