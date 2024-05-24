"""
주식가격
https://school.programmers.co.kr/learn/courses/30/lessons/42584
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.
입출력 예
prices	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
"""

"""
방식은 맞았으나 효율성 탈락
"""
# def solution(prices):
#     # 리스트 전체 길이
#     max_time = len(prices)
#     # 시간, 가격을 담는 배열
#     time_price_list = []
#     # 가격 리스트
#     list_price = [0] * max_time

#     for i in range(max_time):
#         # 현재가
#         now_price = prices[i]

#         # 가격이 1인 경우 떨어질 일이 없음
#         if now_price == 1:
#             list_price[i] = max_time - (i + 1)
#             continue
        
#         # 마지막 값은 0
#         if i - 1 == max_time:
#             continue

#         # [time, price]
#         time_price_list.append([i, now_price])

#         # 처음 들어오는 경우를 제외, 현재 가격과 이전 가격을 비교
#         if i > 0 and now_price < prices[i-1]:
#             # 현재 가격 배열에서 현재가격을 초과하는 모든 가격을 조회
#             target_price_list = [price for price in time_price_list if price[1] > now_price]
#             for target in target_price_list:
#                 time, price = target[0], target[1]
#                 # time 위치의 값을 변경 // 현재 시간에서 배열의 시간을 뺀 값
#                 list_price[time] = i - time
#                 time_price_list.remove(target)
#         # print(time_price_list)
    
#     # 가격이 하락하지 않은 값들의 위치값을 변경
#     for non_target in time_price_list:
#         time, price = non_target[0], non_target[1]
#         list_price[time] = i - time

#     return list_price

"""
stack 활용
"""
def solution(prices):
    list_price = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        # 가격이 바로 하락하는 경우에 대한 처리
        while stack and price < prices[stack[-1]]:
            last_time = stack.pop()
            list_price[last_time] = i - last_time
        stack.append(i)

    # 마지막 까지 남은 값들의 시간값을 변경
    while stack:
        last_time = stack.pop()
        list_price[last_time] = (len(prices) - 1) - last_time

    return list_price

prices = [1, 2, 3, 2, 3, 4, 1]
solution(prices)