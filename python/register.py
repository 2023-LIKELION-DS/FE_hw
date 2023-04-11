print('==============================================')
print('회원가입')
print('==============================================')

register = False

while not register:
    print('회원가입을 진행하시겠습니까? \ny:진행    N:취소')
    register_input = input('>>')
    register_input = register_input.lower()

    if register_input == 'y':
        register = True
        print('==============================================')
        print('회원가입이 진행됩니다.')
        print('==============================================')
    elif register_input == 'n':
        print('==============================================')
        print('회원가입이 취소됩니다..')
        print('==============================================')
        exit()
    else:
        print('입력 값을 확인해주세요.')