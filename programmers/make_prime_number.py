"""
소수 만들기
https://school.programmers.co.kr/learn/courses/30/lessons/12977
"""

import math
from itertools import combinations

def solution(numbers):
    count = 0
    def is_prime_number(num):
        for i in range(2,int(math.sqrt(num)) +1):
            if num % i == 0:
                return False
        return True
        

    # numbers 리스트에서 3개의 요소로 이루어진 모든 조합을 구함
    triplets = combinations(numbers, 3)
    # 각 조합의 합을 계산하여 새 리스트에 저장
    three_sum_list = sorted([sum(triplet) for triplet in triplets])
    for num in three_sum_list:
        if is_prime_number(num):
            count += 1
            
    return count

# 예제
nums = [1, 2, 7, 6, 4]
solution(nums)
