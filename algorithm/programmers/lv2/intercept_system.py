"""
요격시스템
https://school.programmers.co.kr/learn/courses/30/lessons/181188
lv 2
1 ≤ targets의 길이 ≤ 500,000
targets의 각 행은 [s,e] 형태입니다.
이는 한 폭격 미사일의 x 좌표 범위를 나타내며, 개구간 (s, e)에서 요격해야 합니다.
0 ≤ s < e ≤ 100,000,000
"""

    
def solution(targets):
    count = 0
    mis_path = 0

    targets = sorted(targets)
    """
    미사일의 시작점 s가 요격점 안에 포함되어있지 않다면 이동
    미사일이 발사된 지점 s 가 요격점보다 작으면 전부 다 요격됨
    """
    for s, e in targets:
        if mis_path > s:
            mis_path = min(mis_path, e)
        else:
            mis_path = e
            count += 1

    return count

targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
solution(targets)