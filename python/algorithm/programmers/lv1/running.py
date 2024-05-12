"""
달리기 경주
https://school.programmers.co.kr/learn/courses/30/lessons/178871
lv 1
"""

def solution(players, callings):
    # 선수들의 위치를 딕셔너리로 관리
    player_positions = {player: i for i, player in enumerate(players)}
    for player in callings:
        player_index = player_positions[player]
        player_positions[player] -= 1
        player_positions[players[player_index-1]] += 1
        players[player_index - 1], players[player_index] = players[player_index], players[player_index - 1]
        
    return players

# def solution(players, callings):
#     # callings 가 연속으로 몇 번 호출되는지 확인
#     prev_player = callings[0]
#     count = 1
#     for i in range(1, len(callings)):
#         player = callings[i]
#         if callings[i] == prev_player:
#             count += 1
#         else:
#             # 선수 위치 이동
#             # 현재 위치 확인
#             player_index = players.index(prev_player)
#             players.remove(prev_player)
#             players.insert(player_index - count, prev_player)

#             # 다른 값이 나온 경우 초기화
#             prev_player = callings[i]
#             count = 1
#     player_index = players.index(prev_player)
#     players.remove(prev_player)
#     players.insert(player_index - count, prev_player)
#     return players