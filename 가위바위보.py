import random
me = input('가위/바위/보 중에 하나를 선택하시오 ==> ')
cpu = random.choice (['가위','바위','보'])
print(f'컴퓨터 = {cpu}')

if cpu == '가위':
    if me == '바위':
        print('이겼네요!')
    elif me == '가위':
        print('비겼네요')
    elif me == '보':
        print('졌네요 ㅠㅠ')
elif cpu == '바위':
    if me == '보':
        print('이겼네요!')
    elif me == '바위':
        print('비겼네요')
    elif me == '가위':
        print('졌네요 ㅠㅠ')
elif cpu == '보':
    if me == '가위':
        print('이겼네요!')
    elif me == '보':
        print('비겼네요')
    elif me == '바위':
        print('졌네요 ㅠㅠ')