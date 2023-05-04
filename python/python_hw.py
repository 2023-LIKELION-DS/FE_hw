### 문제1 답안 
print("[문제 1]")

dictionary = {
 "국어" : 87,
 "수학" : 88,
 "영어" : 92,
 "과학" : 67,
 "사회" : 72}
print(dictionary)
average = sum(dictionary.values()) / len(dictionary)
print(average)
print('================================================================')

### 문제2 답안
print("[문제 2]")

menus = ['김밥', '라면', '튀김', '떡볶이', '순대']
for menu in menus:
    print(f"오늘의 메뉴:{menu}")
print('================================================================')

### 문제3 답안 
money = 10000
while True:
    print("입금이면 1, 출금이면 2 (종료는 아무거나 누르세요):")
    getout_input = input()

    if getout_input == '1':
        save_money = int(input("금액: "))
        if save_money > 0:
            money += save_money
            print(f"{save_money}원이 입금되었습니다. 현재 잔고는 {money}원입니다.")
        else:
            print("금액을 0보다 크게 입력하세요.")

    elif getout_input == '2':
        out_money = int(input("금액: "))
        if out_money > 0:
            if out_money > money:
                print(f"현재 잔고 부족입니다. {out_money-money}원이 부족합니다.")
            else:
                money -= out_money
                print(f"{out_money}원이 출금되었습니다. 현재 잔고는 {money}원입니다.")
                if money == 0:
                    print("통장을 파기합니다.")
                    break
        else:
            print("금액을 0보다 크게 입력하세요.")

    else:
        print("종료합니다.")
        break
print('================================================================')

### 문제 4 답안
import random
list_menu = []
while True:
            menu = input("추가할 메뉴를 입력하세요.(추가 완료 시 완료를 입력하세요.):")

            if menu == '완료': 
                  break
            else:
                list_menu.append(menu)
                print(f'메뉴판:{list_menu} ')

def table_order():
    num_tables = random.randrange(1, 7)
    for table in range(1, num_tables+1):
        num_orders = random.randrange(1, len(list_menu)+1)
        orders = random.sample(list_menu, num_orders)
        for order in orders:
            print(f'{table}번째 테이블에서 {order}를 주문했습니다.')
            
table_order()
#order은 랜덤하게 잘 나오고 있음!! 
print('================================================================')


### 문제 5-1 답안 
print("[문제 5-1]")

import random

mbti_list = ['ISTJ',
'ISFJ',
'INFJ',
'INTJ',
'ISTP',
'ISFP',
'INFP',
'INTP',
'ESTP',
'ESFP',
'ENFP',
'ENTP',
'ESTJ',
'ESFJ',
'ENTJ']

random_list = []
for i in range(1,201):
      random_list.append(random.choice(mbti_list))
      print(f'{i}번 : {random_list[i-1]}')


### 문제 5-2 답안 
print("[문제 5-2]")


count_dict = {}
for x in mbti_list :
      count_dict[x] = random_list.count(x)

print(count_dict)


### 문제 5-3 답안 
print("[문제 5-3]")

number_mbti = input("mbti를 입력하세요 :").upper()

if number_mbti in count_dict :
     mbti_count = count_dict[number_mbti]
     print(f"{number_mbti}유형의 수 : {mbti_count}")
else:
    print("해당 MBTI 유형이 존재하지 않습니다.")