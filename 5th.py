""" 조건문, 반복문, 문자열, 리스트 """




# def bs31():
#     '''
#     베스킨라빈스31 게임
#     1부터 31까지 숫자를 플레이어들끼리 번갈아 외치다가
#     31을 외치는 사람이 패배하는 게임
# 
#     조건1 : 나의 턴에서 숫자를 직접 입력하며, 숫자 사이에는 space 한 번으로 구분
#     조건2 : 나와 컴퓨터 모두 한 턴에 1회 ~ 3회까지만 숫자를 외칠 수 있음
#     조건3 : 외쳐진 숫자보다 1큰 수만 외칠수 있음 (ex: 5 다음엔 무조건 6)
# 
#     위 조건이 안맞을 경우 다시 입력
#     '''
# 
#     import random
#     # 현재 숫자의 초기화
#     number = 0
# 
#     print("베스킨라빈스 31 게임")
#     print("------------------")
# 
#     while True:
#         # user turn
#         my = input("My turn - 숫자를 입력하세요: ")
#         my = my.split()
# 
#         # 입력된 첫번째 숫자가 현재 상태의 마지막 숫자와 연속이 아니거나 입력된 숫자가 3개 보다 많은 경우 제한
#         if int(my[0]) != number + 1 or len(my) > 3:
#             print("숫자를 제대로 입력하세요")
#             continue
# 
#         # 숫자 2개가 입력되었으나 그것이 연속된 숫자가 아닐 경우 제한
#         if len(my) == 2:
#             if int(my[1]) - int(my[0]) != 1:
#                 print("연속된 숫자만 입력하세요")
#                 continue
# 
#         # 숫자 3개가 입력되었으나 그것이 연속된 숫자가 아닐 경우 제한
#         if len(my) == 3:
#             if (int(my[0]) + int(my[2])) / 2 != int(my[1]):
#                 print("연속된 숫자만 입력하세요")
#                 continue
# 
#         # 정상 입력된 숫자 set의 마지막 숫자를 현재 숫자에 입력
#         number = int(my[-1])
#         print(f"현재 숫자 : {number}")
#         print()
#         print("Computer turn")
# 
#         # 31을 넘겼는지 검사
#         if number >= 31:
#             print("당신의 패배")
#             break
#         
#         # computer turn
#         # computer input list initializing
#         computer = []
# 
#         computer_turn_num = random.randint(1,3)
#         for i in range(computer_turn_num):
#             number += 1
#             # 컴퓨터가 31이 넘는 수를 외치면 31로 되돌리기
#             if number > 31:
#                 number = number - 1
#                 continue
#             computer.append(number)
#             print(f"컴퓨터 : {computer[-1]}")
# 
#         # computer turn이 종료한 후에 최종 number 출력
#         print(f"현재 숫자 : {number}")
#         print(computer)
#         print()
# 
#         # computer input list에 31이 있는지 검사
#         if 31 in computer:
#             print("당신의 승리!")
#             break
# 
#     print("게임 종료")
# 
# bs31()














 
# def grading():
#     '''
#     학생들의 시험 답지와 답안지가 주어졌을 때
#     1) 채점을 하고, 2) 학생들의 점수를 출력하고, 3) 등수도 함께 출력
#     '''
#  
#     # 학생 답지
# #    ans = ["김갑,3242524215",
# #    "이을,3242524223",
# #    "박병,2242554131",
# #    "최정,4245242315",
# #    "정무,3242524315"]
#     ans = ["김갑,3242524315",
#     "이을,3242524223",
#     "박병,2242554131",
#     "최정,4245242315",
#     "정무,3242524315"]
#     
#     # 정답지
#     cor = [3,2,4,2,5,2,4,3,1,2]
# 
#     # 학생, 점수 저장용 dict 초기화
#     full_dict = dict()
#     # 등수 정렬 후 저장용 dict 초기화
#     rank_dict = dict()
# 
#     # 점수 산정 루프
#     for i in ans:
#         name, answer = i.split(',')
#         
#         score = 0
#         for j in range(0, 10):
#             if int(answer[j]) == cor[j]:
#                 score += 10
#         full_dict[name] = score
# 
#     # full_dict 로부터 점수 기준 역순 정렬 후 저장
#     rank_dict = sorted(full_dict.items(), key = lambda item: item[1], reverse = True)
# 
#     # 출력 구문
#     grade = 1
#     code = 1
#     for k in rank_dict:
#         print(f"학생: {k[0]} 점수: {k[1]}점 {grade}등")
#         grade += 1
# 
# #        if code == 1:
# #            tmp_score = k[1]
# #            code = 2
# #            continue
# #
# #        grade -= 1
# #        if tmp_score == k[1] and code 2:
# #            kkkkkkkkkkk
# #            
# #        code = 2
# 
# grading()



 

##### Q3. 숫자 맞추기 게임
#####     컴퓨터가 임의의 숫자를 3개 만들고
#####     사용자가 그것을 맞추는 게임

# 😲조건1 - 숫자는 0 ~ 100까지 숫자를 3개 만듭니다(중복 불가).
# 😲조건2 - 5회, 10회까지 정답을 못맞추면 최솟값, 최대값에 대한 힌트를 줍니다.
# 😲조건3 - 정답을 맞추면, 맞춘 정답이 최솟값인지, 중간값인지, 최댓값인지 알려줍니다.
# import random
# number = random.randint(0, 100)
# ✅출력 예시
# guess_numbers()
# 
# 1차 시도
# 숫자를 예측해보세요 : 39
# 숫자를 맞추셨습니다! 39는 최솟값입니다.
# 2차 시도
# 숫자를 예측해보세요 : 48
# 숫자를 맞추셨습니다! 48는 최댓값입니다.
# 3차 시도
# 숫자를 예측해보세요 : 100
# 숫자를 맞추셨습니다! 100는 최댓값입니다.
# 게임종료
# 3번 시도만에 예측 성공
# 
# ...
# 5차 시도
# 숫자를 예측해보세요 : 9
# 9는 없습니다
# 최솟값은 9보다 작습니다
# 6차 시도
# 숫자를 예측해보세요 : 9
# 이미 예측에 사용한 숫자입니다
# 6차 시도

 

 
#def after_100(mon, day, week):
##### Q4. 날짜를 넣으면 100일 뒤가 몇월 며칠인지
#####     계산해주는 함수

# 😲조건1 - "오늘부터 1일"이기 때문에 날짜를 계산할 때 오늘을 포함합니다
# 😲조건2 - 몇년도인지 구분하지 않고 윤년도 고려하지 않고 2월은 무조건 28일로 합니다.
# 🧐hint
# # 특정 원소의 위치를 찾는 방법
# a = [1,2,3,4]
# a.index(1)
# 0
# ✅출력 예시
# 
# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일

 
mon, day, week = input("월, 일, 요일을 입력 : ").split(',')

mon = int(mon.strip())
day = int(day.strip())
week.rstrip()
# week = week[0]
print(mon, day, week, len(week))
print(week[1])

#after_100(mon, day, week)