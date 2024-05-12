"""
최솟값 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12941
lv 2
"""
def solution(A,B):
    sum_result = 0
    A = sorted(A)
    B = sorted(B, reverse=True)
    for i in range(len(A)):
        sum_result += A[i] * B[i]
    return sum_result


def solutionlambda(A,B):
    return sum(map(lambda a,b : a*b, sorted(A), sorted(B, reverse=True)))

A = [1, 4, 2]
B = [5, 4, 4]

solution(A,B)
