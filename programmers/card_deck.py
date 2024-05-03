"""
카드뭉치
https://school.programmers.co.kr/learn/courses/30/lessons/159994?language=python3
lv 1
"""

def solution(cards1, cards2, goal):
    answer = "Yes"
    def pop_word(word, deck):
        if deck == "deck1" and word == cards1[0]:
            cards1.pop(0)
            return True
        elif deck == "deck2" and word == cards2[0]:
            cards2.pop(0)
            return True
        else:
            return False 
        
    for word in goal:
        if word in cards1:
            word_check = pop_word(word, "deck1")
        elif word in cards2:
            word_check = pop_word(word, "deck2")

        if not word_check:
            answer = "No"

    return answer


# deque 사용
from collections import deque

def solution2(cards1, cards2, goal):
    card1_q = deque(list(cards1))
    card2_q = deque(list(cards2))

    for target in goal:
        if card1_q and card1_q[0] == target:
            card1_q.popleft()
        elif card2_q and card2_q[0] == target:
            card2_q.popleft()
        else:
            return "No"

    return "Yes"

cards1 = ["i", "drink", "water"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(cards1, cards2, goal))