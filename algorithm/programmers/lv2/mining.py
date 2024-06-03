"""
광물 캐기
https://school.programmers.co.kr/learn/courses/30/lessons/172927
곡\광 다 철 돌
다    1  1  1
철    5  1  1
돌    25 5  1
"""

from collections import Counter

def sum_fatigue(pick,mineral_list):
    fatigue = 0
    mineral_counts = Counter(mineral_list)
    count_mineral_list = [mineral_counts["diamond"], mineral_counts["iron"], mineral_counts["stone"]]

    if pick == "diamond":
        fatigue += sum(count_mineral_list)
    elif pick == "iron":
        fatigue += 5 * count_mineral_list[0] + count_mineral_list[1] + count_mineral_list[2]
    else:
        fatigue += 25 * count_mineral_list[0] + 5 * count_mineral_list[1] + count_mineral_list[2]
    return fatigue

def solution(picks, minerals):
    # 사용할 수 있는 총 곡괭이의 개수
    sum_picks = sum(picks)
    # 피로도
    fatigue = 0
    # 돌 곡괭이 기준 광물 가치 계산
    mineral_value = {"diamond" : 25, "iron" : 5, "stone" : 1}
    
    # 5개를 연속으로 채광해야 하므로 5개씩 자른 리스트를 생성
    two_dimension_minerals = [minerals[i:i + 5] for i in range(0, len(minerals), 5)]
    # 사용할 수 있는 곡괭이가 한정되어 있으므로 곡괭이 개수 만큼만 가져옴
    two_dimension_minerals = two_dimension_minerals[:sum_picks]
    # 총 광물 가치가 큰 순으로 정렬
    rank_mineral_list = sorted([(sublist, sum(mineral_value[mineral] for mineral in sublist)) for sublist in two_dimension_minerals],key=lambda x: x[1],reverse=True)
    
    # 좋은 곡괭이부터 순서대로 사용
    for mineral_sum in rank_mineral_list:
        mineral_list = mineral_sum[0]
        if picks[0]:
            fatigue_count = sum_fatigue("diamond", mineral_list)
            picks[0] -= 1
        elif picks[1]:
            fatigue_count = sum_fatigue("iron", mineral_list)
            picks[1] -= 1
        else:
            fatigue_count = sum_fatigue("stone",mineral_list)
            picks[2] -= 1

        fatigue += fatigue_count
        
        if sum_picks == 0:
            break

    return fatigue

picks = [1, 3, 2]
# picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
# minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

solution(picks, minerals)