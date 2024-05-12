"""
데이터 분석
https://school.programmers.co.kr/learn/courses/30/lessons/250121
lv 1
data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
정렬한 데이터들이 담긴 이차원 정수 리스트 data와 어떤 정보를 기준으로 데이터를 뽑아낼지를 의미하는 문자열 ext, 
뽑아낼 정보의 기준값을 나타내는 정수 val_ext, 
정보를 정렬할 기준이 되는 문자열 sort_by가 주어집니다.

data에서 ext 값이 val_ext보다 작은 데이터만 뽑은 후, 
sort_by에 해당하는 값을 기준으로 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해 주세요. 
단, 조건을 만족하는 데이터는 항상 한 개 이상 존재합니다

ext와 sort_by의 값은 다음 중 한 가지를 가집니다.
"code", "date", "maximum", "remain"
순서대로 코드 번호, 제조일, 최대 수량, 현재 수량을 의미합니다.
val_ext는 ext에 따라 올바른 범위의 숫자로 주어집니다.
정렬 기준에 해당하는 값이 서로 같은 경우는 없습니다.
data_example = [code, date, maximum, remain]
"""
def solution(data, ext, val_ext, sort_by):
    case={'code':0,'date':1,'maximum':2,'remain':3}
    standard_target = case.get(ext)
    sort_target = case.get(sort_by)

    sorted_data = sorted([sub_data for sub_data in data if sub_data[standard_target] < val_ext], key=lambda x: x[sort_target])
    return sorted_data

data = [[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]	
ext = "date"
val_ext = 20300501
sort_by = "remain"
result = [[3,20300401,10,8],[1,20300104,100,80]]
print(solution(data,ext,val_ext,sort_by))
