"""
그룹 애너그램
문자열을 애너그램 단위로 그룹핑
lv 2
"""

def solution(word_list):
    anagram_dict = {}
    for word in word_list:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [word]
        else:
            anagram_dict[sorted_word].append(word)
            
    answer = list(anagram_dict.values())

    return answer

word_list = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(solution(word_list))