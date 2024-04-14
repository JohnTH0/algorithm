"""
로그의 가장 앞 부분 = 식별자
문자구성 로그가 숫자 로그보다 앞
식별자는 순서 영향X, 문자가 동일한 경우 식별자 순
숫자 로그는 입력 순
- 추가 조건
혼용은 없는 것으로 생각(내용 X)
"""
example_logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
example_result = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

def solution(logs):
    # 리스트 선언
    str_log_list, num_log_list = [], []
    for log in logs:
        # 숫자 문자 판단
        if log.split()[1].isdigit():
            num_log_list.append(log)
        else:
            str_log_list.append(log)
    # 문자열 로그 정렬
    str_log_list.sort(key=lambda x: (x.split()[1:], x.split()[0:]))
    return str_log_list + num_log_list

solution(example_logs)