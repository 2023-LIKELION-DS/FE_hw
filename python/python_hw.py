"""
##### 문제 1 #####

딕셔너리에 국어: 87, 수학: 88, 영어: 92, 과학: 67, 사회: 72 를 저장하고 평균을 구하시오.

"""
### 문제1 답안 (이 아래에 적어주세요!)
def calAvg():
    score = {"국어": 87, "수학": 88, "영어": 92, "과학": 67, "사회": 72}
    total = sum(score.values())
    avg = total/len(score)
    res = f'5과목의 평균은 {avg}점 입니다.'
    return res

print("[문제 1]")
res = calAvg()
print(res)





"""
##### 문제 2 #####

food = ["김밥", "라면", "튀김", "떡볶이", "순대"]

위 리스트의 요소를 아래와 같은 형식으로 순서대로 출력하시오. 

오늘의 메뉴: 김밥
오늘의 메뉴: 라면
오늘의 메뉴: 튀김
오늘의 메뉴: 떡볶이
오늘의 메뉴: 순대

"""
### 문제2 답안 (이 아래에 적어주세요!)
def menu_print():
    food = ["김밥", "라면", "튀김", "떡볶이", "순대"]
    size = len(food)
    for i in range(0, size):
        print('오늘의 메뉴: ',food[i])

print("[문제 2]")
menu_print()







""" 
##### 문제 3 #####

통장에 10,000원이 들어있다.
사용자로부터 '출금'과 '입금' 중 하나를 입력받고, 입출금시 금액 부분을 입력 받도록 하시오.

입금을 하면 "ㅇㅇㅇ원이 입금되었습니다. 현재 잔고는 ㅇㅇㅇ입니다." 출력
출금을 하면 "ㅇㅇㅇ원이 출금되었습니다. 현재 잔고는 ㅇㅇㅇ입니다." 출력

출금시에 잔고가 부족하면 "현재 잔고 부족입니다. ㅇㅇㅇ원이 부족합니다." 라고 출력
통장잔고가 0원이 되면 "통장을 파기합니다" 출력

사용자로부터 종료 받기 전까지 무한 반복하는 코드 작성



(((( 출력 결과 예시 참고 )))

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 1
금액: -2
금액을 0보다 크게 적으세요.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 1
금액: 5000 
5000원이 입금되었습니다. 현재 잔고는 15000원 입니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 3000
3000원이 출금되었습니다. 현재 잔고는 12000원 입니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 15000
현재 잔고 부족입니다. 3000원이 부족합니다.

입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): 2
금액: 12000
통장을 파기합니다.

"""
### 문제3 답안 (이 아래에 적어주세요!)
def account():
    now = int(10000)
    while True:
        n = int(input("입금이면 1, 출금이면 2 (종료는 아무거나 누르세요): "))
        if n==1:
            while True:
                price = int(input("금액: "))
                if price > 0:
                    break
                else:
                    print("금액을 0보다 크게 적으세요")
            now += price
            print(f"{price}원이 입금되었습니다. 현재 잔고는 {now}원입니다.")
        elif n==2:
            while True:
                price = int(input("금액: "))
                if price > 0:
                    break
                else:
                    print("금액을 0보다 크게 적으세요")
            if price < now:
                now-=price
                print(f'{price}원이 출금되었습니다. 현재 잔고는 {now}원입니다.')
            elif price == now:
                now-=price
                print('통장을 파기합니다.')
            elif price > now:
                bal = price - now
                print(f'현재 잔고 부족입니다. {bal}원이 부족합니다.')
        else:
            print('프로그램을 종료합니다.')
            break

print("[문제 3]")
account()





"""
##### 문제 4 #####

메뉴판에 메뉴를 추가하세요. 
추가를 완료하면 각 테이블에서 어떤 주문을 했는지 랜덤으로 출력되게 하세요. (테이블은 총 6개가 있습니다. 단, 몇 개의 테이블에서 주문하는지도 랜덤입니다.)

6개의 테이블 중 몇 개의 테이블에서 주문할지, 주문 내역이 랜덤값입니다.

힌트: import random, randomrange


(((( 출력 결과 예시 참고 )))

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 순대
메뉴판:  ['순대']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 튀김
메뉴판:  ['순대', '튀김']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 라면
메뉴판:  ['순대', '튀김', '라면']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 김밥
메뉴판:  ['순대', '튀김', '라면', '김밥']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 떡볶이
메뉴판:  ['순대', '튀김', '라면', '김밥', '떡볶이']

추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): 완료

1번째 테이블에서 김밥를 주문했습니다.
2번째 테이블에서 김밥를 주문했습니다.
3번째 테이블에서 떡볶이를 주문했습니다.

"""
### 문제4 답안 (이 아래에 적어주세요!)
import random
def order():
    menu_list = []
    while True:
        menu = input("추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.): ")
        if menu =='완료':
            break
        else:
            menu_list.append(menu)
            print(menu_list)

#1-6 중 랜덤값 받아서 그거만큼 반복문 근데 이제 menu_list 에서 값 랜덤으로 뽑아오기
    n = random.randrange(1,7)
    for i in range(1,n+1):
        choice = random.choice(menu_list)
        print(f'{i}번째 테이블에서 {choice}을(를) 주문했습니다.')

print("[문제 4]")
order()





"""
##### 문제 5-1 #####

mbti의 검사결과는 아래와 같이 16가지 유형이 있다.
'ISTJ'
'ISFJ'
'INFJ'
'INTJ'
'ISTP'
'ISFP'
'INFP'
'INTP'
'ESTP'
'ESFP'
'ENFP'
'ENTP'
'ESTJ'
'ESFJ'
'ENTJ'

이때, 200명의 mbti 검사결과를 random 하게 만드는 함수를 작성해보세요

출력 조건) 200명의 검사 결과는 list로 담는다
힌트) 문자열을 랜덤하게 출력하는 코드는 아래와 같습니다.
import random

hint = "ABCDEFGH"
random.choice(hint)

"""
### 문제 5-1 답안 (이 아래에 적어주세요!)
print("[문제 5-1]")

import random
mbti_list = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP', 'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENTJ', 'ENFJ']
mbti_res = []
def mbti_test():
    for i in range(0,200):
        choice = random.choice(mbti_list)
        mbti_res.append(choice)
        print(f'{i+1}번 : {mbti_res[i]}')
    # print(mbti_res) #리스트 형식으로 출력
mbti_test()


"""
##### 문제 5-2 #####

200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.

"""
### 문제 5-2 답안 (이 아래에 적어주세요!)
def mbti_count(test_list):
    # test_list = mbti_test()
    mbti_dic = {}
    for x in test_list:
        if x in mbti_dic:
            mbti_dic[x] += 1
        else:
            mbti_dic[x] = 1
    return mbti_dic
    
print("[문제 5-2]")
# mbti_test() #문제 5-1과 이어져 출력되므로, 생략
test_list = mbti_res
mbti_dic = mbti_count(test_list)
print(test_list)
print(mbti_dic)



"""
##### 문제 5-3 #####

mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것

"""
### 문제 5-3 답안 (이 아래에 적어주세요!)
def mbti_find(getMbti, mbti_dic):
    for key in mbti_dic:
        if key==getMbti:
            return mbti_dic.get(key)
print("[문제 5-3]")
getMbti = input("16가지 유형의 mbti 중 하나를 입력하세요.(ex: ISFP, intp etc.) : ").upper()
count_res = mbti_find(getMbti, mbti_dic)
print(f'{getMbti} 유형에는 {count_res}명이 해당됩니다.')
