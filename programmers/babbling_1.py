"""
https://school.programmers.co.kr/learn/courses/30/lessons/120956
옹알이 (1)
"aya", "ye", "woo", "ma"
"""

def solution(babbling:list) -> int:
    count = 0
    for bab in babbling:
        bab_check_str = ""
        for i in range(len(bab)):
            bab_check_str += bab[i]
            if bab_check_str in ["aya", "ye", "woo", "ma"]:
                bab_check_str = ""

        if bab_check_str == "":
            count +=1

    return count

babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
solution(babbling)