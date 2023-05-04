import random

list_menu = []

while True:
    menu = input("추가할 메뉴를 입력하세요. (추가 완료 시 '완료'를 입력하세요.): ")
    if menu == '완료':
        break
    else:
        list_menu.append(menu)
        print(f'메뉴판: {list_menu}')

def table_order():
    num_tables = random.randrange(1, 7)
    for table in range(1, num_tables+1):
        num_orders = random.randrange(1, len(list_menu)+1)
        orders = random.sample(list_menu, num_orders)
        for order in orders:
            print(f'{table}번째 테이블에서 {order}를 주문했습니다.')
            
table_order()
