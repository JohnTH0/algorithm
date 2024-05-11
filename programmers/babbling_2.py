"""
https://school.programmers.co.kr/learn/courses/30/lessons/133499
옹알이 (2)
lv 1
"""
def solution(babbling:list) -> int:
    count = 0
    for bab in babbling:
        bab_check_str = ""
        previous_str = ""
        for i in range(len(bab)):
            bab_check_str += bab[i]
            if bab_check_str in ["aya", "ye", "woo", "ma"] and not previous_str == bab_check_str:
                previous_str = bab_check_str
                bab_check_str = ""

        if bab_check_str == "":
            count +=1
    return count

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
solution(babbling)