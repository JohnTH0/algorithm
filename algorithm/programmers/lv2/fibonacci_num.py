"""
피보나치 수
https://school.programmers.co.kr/learn/courses/30/lessons/12945
https://www.geeksforgeeks.org/python-program-for-n-th-fibonacci-number/
lv 2
"""

"""
2 이상의 n번째 피보나치 수 에서 n-2, n-1을 n번째 까지 반복하여 값을 저장 후 더하는 식으로 추출
0, 1 이 초기값인 이유는 가장 처음 수
"""

def fibonacci(n):
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b % 1234567

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return b
