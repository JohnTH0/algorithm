"""
붕대 감기
https://school.programmers.co.kr/learn/courses/30/lessons/250137
lv 1
bandage	health	attacks	result
[5, 1, 5]	30	[[2, 10], [9, 15], [10, 5], [11, 5]]	5
"""
# def solution(bandage, health, attacks):
#     # 공격하는 시간
#     attack_time = [time[0] for time in attacks]
#     # 최대 초 길이
#     attack_range = int(sorted(attacks)[-1][0]) + 1
#     heal_bonus_count = 0
#     max_health = health
#     for time in range(0, attack_range):
#         # 확인 순서 : 공격체크, 회복체크
#         # 최대체력을 초과하여 회복할 수 없음
#         # 공격하지 않음 = 체력 회복
#         if not time in attack_time:
#             # 최대 체력이 아닌 경우, 회복카운트 확인 후 회복 진행
#             heal_bonus_count += 1
#             if heal_bonus_count == bandage[0]:
#                 heal = bandage[1] + bandage[2]
#                 heal_bonus_count = 0
#             else:
#                 heal = bandage[1]
#             # 회복은 최대체력까지만 회복 가능 
#             health = health + heal if health + heal <= max_health else max_health
#         # 공격하는 경우 공격 진행
#         # 공격받는 경우 체력은 회복하지 않는다
#         else:
#             # 공격받는 경우 체력 보너스 카운트는 초기화 된다.
#             heal_bonus_count = 0
#             # 대미지 계산
#             damage_list = [val for val in attacks if val[0] == time]
#             damage = damage_list[0][1]
#             health = health - damage if health - damage > 0 else -1
#             if health == -1:
#                 return health
#     return health



# 다른 사람 풀이 중 참고
def solution(bandage, health, attacks):
    hp = health
    start = 1
    for i, j in attacks:
        print("공격시간 i :::", i)
        print("공격대미지 j :::", j)
        print("start:::", start)
        print("이전 체력::",hp)
        print(i - start)
        # 공격받기 전까지 회복량 계산
        hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1] # 0 + 1
        """
        i 는 현재 시간
        start는 이전 공격 시간
        i - start 로 이전 공격까지의 텀 계산
        ((i - start) // bandage[0]) * bandage[2] 보너스를 받기 전까지의 텀 계산
        (i - start) * bandage[1] 초당 회복량 * 공격까지의 텀
        """
        start = i + 1
        print("after start:::", start)

        if hp >= health:
            hp = health
        hp -= j
        print("공격받은 후 체력::",hp)
        print("\n")
        if hp <= 0:
            return -1
    return hp

bandage = [5, 1, 5]
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
health = 30

print(solution(bandage, health, attacks))
