"""
과제 진행하기
https://school.programmers.co.kr/learn/courses/30/lessons/176962
과제는 시작하기로 한 시각이 되면 시작합니다.
새로운 과제를 시작할 시각이 되었을 때, 기존에 진행 중이던 과제가 있다면 진행 중이던 과제를 멈추고 새로운 과제를 시작합니다.
진행중이던 과제를 끝냈을 때, 잠시 멈춘 과제가 있다면, 멈춰둔 과제를 이어서 진행합니다. 멈춘 과제는 중간부터 시작
만약, 과제를 끝낸 시각에 새로 시작해야 되는 과제와 잠시 멈춰둔 과제가 모두 있다면, 새로 시작해야 하는 과제부터 진행합니다.
멈춰둔 과제가 여러 개일 경우, 가장 최근에 멈춘 과제부터 시작합니다.
"""

def solution(plans):
    # plans를 시작하는 시간 순서대로 정렬
    plans = sorted(plans, key=lambda x: (int(x[1].split(":")[0]), int(x[1].split(":")[1])))
    # print(plans)

    # 중간에 멈춘 과제 리스트
    pause_plan = []
    # 완료한 과제
    answer_plan = []

    for i in range(len(plans)):

        # 현재 과제
        plan = plans[i]

        # 마지막인 경우
        if i + 1 == len(plans):
            answer_plan.append(plan[0])
            continue

        # 다음 과제
        next_plan = plans[i+1]
        # 시작시간
        start_time = int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1])
        # 소요시간
        process_time = int(plan[2])
        result_time = start_time + process_time

        # 다음과제의 시작시간
        next_project_start_time = int(next_plan[1].split(":")[0]) * 60 + int(next_plan[1].split(":")[1])
         
        # 다음과제 까지의 남은 시간
        remain_time = next_project_start_time - result_time

        # 같거나 큰 경우, 해당 작업 완료 후, 다음 작업 전까지의 중단한 작업 확인
        if remain_time >= 0:
            answer_plan.append(plan[0])

            # 중단한 작업이 있는 경우 가장 최근에 멈춘 과제부터 확인
            while pause_plan and remain_time > 0:
                # 남은 시간에서 계산
                if remain_time >= pause_plan[-1][1]:
                    remain_time -= pause_plan[-1][1]
                    answer_plan.append(plans[pause_plan[-1][0]][0])
                    pause_plan.pop()
                else:
                    pause_plan[-1][1] -= remain_time
                    break
                
        # 작은 경우, 완료하지 못하였으므로 남은 시간을 적립
        else:
            pause_plan.append([i,process_time - (next_project_start_time - start_time)])

    # 중단한 작업이 있는 경우 가장 최근에 멈춘 과제부터 확인
    while pause_plan:
        answer_plan.append(plans[pause_plan[-1][0]][0])
        pause_plan.pop()

    print(answer_plan)
    return answer_plan

plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
# plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
# plans = [["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]

solution(plans)