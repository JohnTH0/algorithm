"""
개인정보 수집 유효기간
https://school.programmers.co.kr/learn/courses/30/lessons/150370
lv 1
"""

from datetime import datetime

def solution(today, terms, privacies):
    # 형변환 및 기간 정보를 dict로 전환
    today = datetime.strptime(today,"%Y.%m.%d")
    terms_dict = {term.split()[0] : term.split()[1] for term in sorted(terms,key=lambda x : x[0])}
    answer = []

    # 주어진 날짜를 일수로 변경
    def calculate_date(date, after_month=0):
        year = date.year
        month = date.month
        day = date.day
        total_days = (year * 12 * 28) + (month * 28) + (after_month * 28) + day
        return total_days

    for idx, privacy in enumerate(privacies):
        privacy_date = datetime.strptime(privacy.split()[0],"%Y.%m.%d")
        option = privacy.split()[1]
        if calculate_date(privacy_date, int(terms_dict[option])) <= calculate_date(today):
            answer.append(idx+1)

    return sorted(answer)

today = "2020.01.01"   
terms = ["Z 3", "D 5"]   
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]   
solution(today, terms, privacies)
