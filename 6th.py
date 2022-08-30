# """
# 딕셔너리는 순서가 없는 것이 맞지만
# Python 3.7 버젼 이후로는 딕셔너리가 입력된 순서대로 출력이 됩니다.
# 강의에서는 3.6버젼이 사용된 것으로 보입니다.
# 
# a = {"a": 1 , "b": 22, "c": 15}
# print(list(a))
# ["a", "b", "c"]
# 이점을 참고하시어 미션을 풀어 보시길 바랍니다.
# """ 
# 
# 
# """ Q1. 
# 고려시대와 조선시대 왕 이름 중
# 고려에도 있고 조선에도 있는 이름은 몇개 일까요?
# 한 번에 딱 안 떠오른다면 왕 이름을 드릴테니 파이썬 함수로 만들어서 출력 해봅시다.
# 
# 조건1 - 중복되는 왕 이름 출력
# 조건2 - 중복되는 왕 이름의 수 출력
# 주의 : 고려에 이름이 같은 왕 "정종" 고려할 것.
# """
# count = 0
# korea_king = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
# chosun_king = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
# 
# kk_list = korea_king.split(',')
# ck_list = chosun_king.split(',')
# du_list = []
# 
# for name in kk_list:
#     if name not in du_list and name in ck_list:
#         count += 1
#         print("조선과 고려에 모두 있는 왕 이름 : ", name)
#         du_list.append(name)
# 
# print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")







# def king(korea, chosun):
#     king_dict = dict() # 왕 이름을 담을 dict
#     
#     korea = korea.split(",") # 문자열을 ,기준으로 list 변경 
#     chosun = chosun.split(",") # 문자열을 ,기준으로 list 변경
#     
#     # 고려의 왕 이름 저장 후 값을 1로 설정
#     for name in korea:
#         king_dict[name] = 1
# 
#     # 조선의 왕 탐색
#     for cho in chosun:
#         if king_dict.get(cho, 0) >= 1: # 왕 이름이 존재 여부 있으면 1이상의 값이 나옴
#             king_dict[cho] = king_dict[cho] + 1 # 존재하면 +1
#         else:
#             continue # 없으면 건너 뜀
# 
# #    리스트 컴프리헨션을 사용하면 아래 코드
#     repeated_king = [ k for (k, v) in king_dict.items() if v >= 2 ]
#     
# #    repeated_king = [] # 중복된 왕 이름을 담는 리스트
# #    for (k,v) in king_dict.items():
# #        if v >= 2: # 왕 이름이 2이상이면 중복된 것
# #            repeated_king.append(k)
#     
#     count = 0 # 카운트 변수
#     for king in repeated_king:
#         print(f"조선과 고려에 모두 있는 왕 이름 : {king}")
#         count = count + 1 # 존재하면 +1
#     print(f"조선과 고려에 모두 있는 왕 이름은 총 {count}개 입니다")
# 
# korea = "태조,혜종,정종,광종,경종,성종,목종,현종,덕종,정종,문종,순종,선종,헌종,숙종,예종,인종,의종,명종,신종,희종,강종,고종,원조,충렬왕,충선왕,충숙왕,충혜왕,충목왕,충정왕,공민왕,우왕,창왕,공양왕"
# chosun = "태조,정종,태종,세종,문종,단종,세조,예종,성종,연산군,중종,인종,명종,선조,광해군,인조,효종,현종,숙종,경종,영조,정조,순조,헌종,철종,고종,순종"
# king(korea, chosun)




# def sales_management(member_names, member_records):
#     """ Q2.
#     6명의 멤버를 거느리는 영업팀의 영업관리자...
#     각 멤버별로 올해 실적을 보고
#     잘한 멤버는 보너스를 주고
#     못한 멤버는 면담을 하려고 합니다.
#     
#     보너스 대상자와 면담 대상자를 골라주세요.
#     
#     조건 1 - 예비 보너스 대상자는 평균 실적 1등 2등 입니다.
#     조건 2 - 예비 면담 대상자는 평균 실적 5등 6등 입니다.
#     조건 3 - 보너스 대상자의 평균 실적이 5보다 크지 않으면 보너스 대상자에서 제외 됩니다.
#     조건 4 - 면담 대상자의 평균 실적이 3보다 크면 면담 대상자에서 제외 됩니다.
#     """
# 
#     count = 0
#     record = [0, 0]
#     score_tmp = {}
#     rank_tmp = {}
# 
#     for i in member_records:
#         for j in i:
#             record[0] = record[0] + j
#             count += 1
#         record[1] = record[0] / count
# 
#         score_tmp[member_names[member_records.index(i)]] = record
#         count = 0
#         record = [0, 0]
#     
# 
#     # full_dict 로부터 점수 기준 역순 정렬 후 저장
#     rank_tmp = sorted(score_tmp.items(), key = lambda item: item[1][0], reverse = True)
# 
#     for i in rank_tmp:
#         if rank_tmp.index(i) <= 1 and i[1][1] > 5:
#             print(f"보너스 대상자 {i[0]}")
#         else:
#             break
# 
#     for j in reversed(rank_tmp):
#         if rank_tmp.index(j) >= -2 and j[1][1] <= 3:
#             print(f"면담 대상자 {j[0]}")
#         else:
#             break
# 
# # 이름, 실적
# member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
# member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],
#                   [2,3,4,3,1,2,0,3,2,5,7,2],
#                   [1,3,0,3,3,4,5,6,7,2,2,1],
#                   [3,2,9,2,3,5,6,6,4,6,9,9],
#                   [8,7,7,5,6,7,5,8,8,6,10,9],
#                   [7,8,4,9,5,10,3,3,2,2,1,3]]
# sales_management(member_names, member_records)







#def stock_profit(stocks, sells):
#    """ Q3
#    예금 금리가 너무 낮아서 주식을 시작했습니다.
#    아래와 같이 매수 종목, 수량, 평균 매수 금액이 있습니다.
#    판매가는 따로 주어집니다.
#    종목과 수익률만 출력하시고 종목별 수익률이 높은 순서대로 출력해주세요.
#    (소수 둘째자리까지 출력)
#    """
#
#    stock_list = {}
#
#    tmp_list = stocks.split(',')
#    
#    for i in tmp_list:
#        j = i.split('/')
#        earning = (sells[tmp_list.index(i)] / int(j[2]) - 1) * 100
#        stock_list[j[0]] = [int(j[1]), int(j[2]), sells[tmp_list.index(i)], earning]
#
#    # full_dict 로부터 점수 기준 역순 정렬 후 저장
#    rank_list = sorted(stock_list.items(), key = lambda item: item[1][3], reverse = True)
#
#    for k in rank_list:
#        print(f"{k[0]}의 수익률 {k[1][3]:.3}")
#
#stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
#sells = [82000, 160000, 835000, 410000]
#stock_profit(stocks, sells)
#
## # 소수 둘째자리까지 출력하는 방법
## a = 3.141592
## print(f"{a:.3}")
## 3.14












def good_customer(info):
    """ Q04
    여러분은 상품 판매자입니다.
    매월 상품을 많이 구매해준 VIP회원에게 할인 쿠폰을 제공해주려고 합니다.
    아래와 같은 회원 정보가 있을 때 회원 정보를 출력하고
    할인 쿠폰을 받을 회원이 누구인지 출력하는 함수를 만들어 주세요.
    
    조건1 - 8회 이상 구매한 회원이 VIP대상
    조건2 - 전화번호가 없으면 쿠폰을 받을 수 없음
    조건3 - 전화번호가 없으면 000-0000-0000으로 출력할 것
    """

    info_list = []
    idd = []
    age = []
    tel = []
    gender = []
    zone = []
    number = []
    clint_info = {}
    
    tmp_list = info.split(',')
    for i in tmp_list: 
        if tmp_list.index(i)%6 == 2 and i == 'x':
            i = '000-0000-0000'
        info_list.append(i.strip())

    for j in info_list: 
        match info_list.index(j)%6:
            case 0: idd.append(j)
            case 1: age.append(j)
            case 2: tel.append(j)
            case 3: gender.append(j)
            case 4: zone.append(j)
            case 5: number.append(j)

    clint_info["아이디"] = idd
    clint_info["나이"] = age
    clint_info["전화번호"] = tel
    clint_info["성별"] = gender
    clint_info["지역"] = zone
    clint_info["구매횟수"] = number

    for k in clint_info["구매횟수"]:
        if int(k) >= 8 and clint_info["전화번호"][clint_info["구매횟수"].index(k)] != "000-0000-0000":

            print("할인 쿠폰을 받을 회원정보")
            print("아이디   : ", clint_info["아이디"][clint_info["구매횟수"].index(k)])
            print("나이     : ", clint_info["나이"][clint_info["구매횟수"].index(k)])
            print("전화번호 : ", clint_info["전화번호"][clint_info["구매횟수"].index(k)])
            print("성별     : ", clint_info["성별"][clint_info["구매횟수"].index(k)])
            print("지역     : ", clint_info["지역"][clint_info["구매횟수"].index(k)])
            print("구매횟수 : ", clint_info["구매횟수"][clint_info["구매횟수"].index(k)])
            print()

# 회원은 6명이고, "아이디, 나이, 전화번호, 성별, 지역, 구매횟수" 순으로 입력되어 있음
info = """abc,21세,010-1234-5678,남자,서울,5,
        cdb,25세,x,남자,서울,4,
        bbc,30세,010-2222-3333,여자,서울,3,
        ccb,29세,x,여자,경기,9,
        dab,26세,x,남자,인천,8,
        aab,23세,010-3333-1111,여자,경기,10"""
good_customer(info)
 














