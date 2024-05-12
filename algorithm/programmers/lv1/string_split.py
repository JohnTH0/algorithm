"""
문자열 나누기
https://school.programmers.co.kr/learn/courses/30/lessons/140108
lv 1
s	result
"banana"	3
"abracadabra"	6
"aaabbaccccabba"	3
aaabbacc / ccab / ba
"""

def solution(s):
    s_len = len(s)
    s_list = list(s)
    target_s_list = []
    first_s = ""
    count = 0
    for i in range(s_len):
        s_word = s_list[i]
        target_s_list.append(s_word)

        if len(target_s_list) > 1 :
            first_s = target_s_list[0]
            first_s_len = len([val for val in target_s_list if val == first_s])
            else_s_len = len([val for val in target_s_list if not val == first_s])
            if first_s_len == else_s_len:
                count += 1
                target_s_list = []
    
    if not len(target_s_list) == 0:
        count +=1

    return count

