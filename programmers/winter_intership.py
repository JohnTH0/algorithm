"""
가장 많이 받은 선물
2024 kakao winter intership
https://school.programmers.co.kr/learn/courses/30/lessons/258712
lv 1
두 사람이 선물을 주고받은 기록이 있다면, 이번 달까지 두 사람 사이에 더 많은 선물을 준 사람이 다음 달에 선물을 하나 받습니다.
두 사람이 선물을 주고받은 기록이 하나도 없거나 주고받은 수가 같다면, 
선물 지수가 더 큰 사람이 선물 지수가 더 작은 사람에게 선물을 하나 받습니다.
선물 지수는 이번 달까지 자신이 친구들에게 준 선물의 수에서 받은 선물의 수를 뺀 값입니다.
만약 두 사람의 선물 지수도 같다면 다음 달에 선물을 주고받지 않습니다.
이때, 다음달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 return
gifts ["muzi frodo"] = A가 B에게 선물
"""

# 해당 함수 확인
"""
list(zip(*g)) = 들어오는 배열을 세로로 묶어줌
"""
def gift_point(gift_list, i):
    return sum(gift_list[i]) - sum(list(zip(*gift_list))[i])


def solution(friends, gifts):
    answer = 0
    friends_len = len(friends)

    # 배열 생성
    gift_list = [[0] * friends_len for _ in range(friends_len)]

    # 친구 순서대로 번호 부여
    friend_dict = {}

    for i, friend in enumerate(friends):
        friend_dict[friend] = i

    for gift in gifts:
        a, b = gift.split(" ")
        x, y = friend_dict[a], friend_dict[b]
        gift_list[x][y] += 1

    gift_result = [0] * friends_len

    for i in range(friends_len):
        for j in range(i+1, friends_len):
            a, b = gift_list[i][j], gift_list[j][i]
            if a>b:
                gift_result[i] += 1
            elif a<b:
                gift_result[j] += 1
            else:
                i_gp = gift_point(gift_list, i)
                j_gp = gift_point(gift_list, j)
                if i_gp > j_gp:
                    gift_result[i] += 1
                elif i_gp < j_gp:
                    gift_result[j] += 1

    answer = max(gift_result)

    return answer


friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

solution(friends, gifts)
