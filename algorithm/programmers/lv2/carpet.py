"""
카펫
https://school.programmers.co.kr/learn/courses/30/lessons/42842
lv 2
"""

def solution(brown, yellow):
    # 전체 격자 개수를 w * h 라고 할때,
    # brown = 2 * w + 2 * h - 4 (테두리 격자의 수)
    # yellow = (w - 2) * (h - 2) (내부 격자의 수)
    total = brown + yellow
    
    # yellow길이가 1인 경우, 최소 brown의 길이는 3부터 
    for height in range(3, total // 3 + 1):
        # 나머지가 0 인 경우에 사각형이 되고, 이 경우에 주어진 조건을 만족하는 경우를 확인
        if total % height == 0:
            width = total // height
            if (width - 2) * (height - 2) == yellow:
                return [width, height]

brown = 24
yellow = 24 
solution(brown, yellow)