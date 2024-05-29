"""
카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
lv 2
"""

import math
def solution(brown, yellow):
    sum_grid = brown + yellow
    def prime_factors(n):
        factors = []
        i = 2
        while i <= n:
            if n % i == 0:
                factors.append(i)
                n = n / i
            else:
                i = i + 1
        return factors
    
    factors = sorted(prime_factors(sum_grid))
    print(factors)
    import time
    i = 1
    while True:
        brown_rows, yellow_rows = math.prod(factors[:i]), math.prod(factors[i:])
        print(brown_rows)
        print(yellow_rows)
        time.sleep(1)
        if yellow_rows + 2 == brown_rows:
            break
        i += 1


brown = 48
yellow = 48
solution(brown, yellow)