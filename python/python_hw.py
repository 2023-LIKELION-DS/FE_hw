"""
##### 문제 1 #####
 
딕셔너리에 국어: 87, 수학: 88, 영어: 92, 과학: 67, 사회: 72 를 저장하고 평균을 구하시오.

"""
### 문제1 답안 (이 아래에 적어주세요!)
print("[문제 1]")

score={'국어':87,'수학':88,'영어':92,'과학':67,'사회':72}
ave=sum(score.values())/len(score)
print(ave)


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
print("[문제 2]")

food = ["김밥", "라면", "튀김", "떡볶이", "순대"]

for i in range(0,5,1):
    print("오늘의 메뉴:",food[i])





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
print("[문제 3]")
total_money=10000
while(True):
    a=int(input("입금이면 1, 출금이면 2(종료는 아무거나 누르세요):"))
    money=0
    if a==1:
            money=int(input("입금 금액을 적어주세요: "))
            if money>0:
                print("금액:",money)
                total_money += money
                print(money,"원이 입금되었습니다. 현재 잔고는 ",total_money,"원 입니다.\n")
                continue
            else:
                print("금액을 0보다 크게 적으세요.\n")
                continue

    elif a==2:
            money=int(input("입금 금액을 적어주세요: "))
            print("금액:",money)
            if money>0:
                if (total_money-money)>0:
                    total_money -= money
                    print(money,"원이 출금되었습니다. 현재 잔고는 ",total_money,"원 입니다.\n")
                    continue
                elif (total_money-money)<0:
                    need_money=money-total_money
                    print("현재 잔고 부족입니다.",need_money,"원이 부족합니다.\n")
                    continue
                elif total_money==money:
                    print("통장을 파기합니다.\n")
                    continue
            else:
                print("금액을 0보다 크게 적으세요.\n")
                continue

    else:
            a=False
            break




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
print("[문제 4]")
want=[]

while True:
    menu=input("추가할 메뉴를 입력하세요.(추가 완료 시 '완료'를 입력하세요.):")
    if menu!='완료':
        want.append(menu)
        print("메뉴판:",want)
        continue
    elif menu=='완료':
        False
        

    import random
    people = random.randrange(1,6)


    for i in range(1,(people+1),1):
        import random
        food=random.choice(want)
        print(i,"번째에서",food,"를 주문했습니다.")

    break


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
mbti=['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENTJ']
mbti_people=[]
for i in range(1,101,1):
    import random
    mbti_who=random.choice(mbti)
    mbti_people.append(mbti_who)

print(mbti_people)


"""
##### 문제 5-2 #####

200명의 검사 결과가 각 16가지의 유형별 몇 명이 있는지 구하기

출력 조건) 딕셔너리 형식( {'mbti유형': 총 명수})
출력 예시) {'ESFP':17, 'INFJ': 13...}
힌트) 각각의 mbti 유형을 세는 법(counting)을 생각해보자.

"""
### 문제 5-2 답안 (이 아래에 적어주세요!)
print("[문제 5-2]")
number_istj=mbti_people.count('ISTJ')
number_isfj=mbti_people.count('ISFJ')
number_infj=mbti_people.count('INFJ')
number_intj=mbti_people.count('INTJ')
number_istp=mbti_people.count('ISTP')
number_isfp=mbti_people.count('ISFP')
number_infp=mbti_people.count('INFP')
number_intp=mbti_people.count('INTP')
number_estp=mbti_people.count('ESTP')
number_esfp=mbti_people.count('ESFP')
number_enfp=mbti_people.count('ENFP')
number_entp=mbti_people.count('ENTP')
number_estj=mbti_people.count('ESTJ')
number_esfj=mbti_people.count('ESFJ')
number_entj=mbti_people.count('ENTJ')

final_mbti={'ISTJ':number_istj,'ISFJ':number_isfp,'INFJ':number_infj,'INTJ':number_intj,'ISTP':number_istp,'ISFP':number_isfp,'INFP':number_infp,'INTP':number_intp,'ESTP':number_estp,'ESFP':number_esfp,'ENFP':number_enfp,'ENTP':number_entp,'ESTJ':number_estj,'ESFJ':number_esfj,'ENTJ':number_entj}

print(final_mbti)


"""
##### 문제 5-3 #####

mbti 유형을 딕셔너리의 key로 입력했을 경우, value로 몇 명이 해당 mbti에 속해있는지 출력하는 함수를 작성
출력 조건) 알파벳 입력시 대,소문자는 결과에 영향을 미치지 않도록 코드를 작성할 것

"""
### 문제 5-3 답안 (이 아래에 적어주세요!)
print("[문제 5-3]")

mbti_what=input('mbti 유형을 입력하세요: ')
mbti_what=mbti_what.upper()

print(mbti_what,":",final_mbti[mbti_what])