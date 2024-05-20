"""
영어 끝말잇기
https://school.programmers.co.kr/learn/courses/30/lessons/12981
lv 2
return [x, y]
x번째 사람의 y번째순 탈락
2 <= n <= 10 
"""

def solution(n, words):
    word_list = []

    for i in range(len(words)):
        word = words[i]

        first_word = list(word)[0]
        previous_last_word = list(words[i-1])[-1]
        if 0 < i <= len(words) -1:

            if word in word_list or first_word != previous_last_word:
                division, remainder = divmod((i), n)

                return [remainder + 1, division + 1]

        word_list.append(word)
        
    return [0, 0]

words = ["hello", "one", "even", "never", "now", "world", "draw"]	
n = 2