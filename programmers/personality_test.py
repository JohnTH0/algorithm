"""
성격유형 검사하기
https://school.programmers.co.kr/learn/courses/30/lessons/118666
lv 1
1	매우 비동의     3
2	비동의          2
3	약간 비동의     1 
4	모르겠음        0
5	약간 동의       1
6	동의            2
7	매우 동의       3
"""
 
def solution(survey, choices):
    indicators_str = ''
    survey_scores = {
        "R" : 0,
        "T" : 0,
        "C" : 0,
        "F" : 0,
        "J" : 0,
        "M" : 0,
        "A" : 0,
        "N" : 0
        }
    
    choice_score_dict = {
            1:3, 
            2:2,
            3:1, 
            4:0, 
            5:-1,
            6:-2,
            7:-3
        }

    for i in range(len(survey)):
        survey_scores[survey[i][0]] += choice_score_dict[choices[i]]

    indicators_str += "R" if survey_scores["R"] >= survey_scores["T"] else "T"
    indicators_str += "C" if survey_scores["C"] >= survey_scores["F"] else "F"
    indicators_str += "J" if survey_scores["J"] >= survey_scores["M"] else "M"
    indicators_str += "A" if survey_scores["A"] >= survey_scores["N"] else "N"

    return indicators_str

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

solution(survey, choices)