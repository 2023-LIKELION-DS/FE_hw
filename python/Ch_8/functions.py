# 함수(Functions)
# 매개변수(파라미터), 인자(인수)

# 'name' => 파라미터
def print_name(name) :
    print(f'이름은 {name}입니다')

# "김멋사", "이멋사" => 인자(인수)
# print_name("김멋사")
# print_name("이멋사")

def print_ex_string() :
    print('예시 문자열입니다.')

# print_ex_string()

def print_name_age(name, age) :
    print(f'이름은 {name}이고 {age}살 입니다.')

# print_name_age("김멋사", "28")

def order_coffee(qty, option='hot') : # 지정해주고 싶다면 뒤에 위치
    print(f'{qty}잔 / {option}')

# order_coffee(3, 'iced')
# order_coffee(3)
# order_coffee(option='iced', qty=5) # 순서는 바뀌었지만 정상적 작동


def get_id(email) :
    if email.endswith('@test.com') :
        email_id = email.removesuffix('@test.com')
        print(email_id)
        return email_id
    else :
        print('처리할 수 없는 이메일 주소입니다.')

user_id = get_id('user@test.com')
print(user_id)

# user_id_2 = get_id('user@example.com')
# print(user_id_2)