#03/11==============================================================================================================

#input()함수는 키보드 입력을 받음
#키보드 입력에는 숫자 뿐만 아니라 문자열도 있음
#input() 함수는 입력된 값이 숫자인지 문자열인지 구분x

#num1 = input()
#num2 = 200
#print(num1, '+', num2)

#그러므로 값을 받은 이후에 형변환이 필요한 경우 변환을 해줘야함
#num1 = int(input('숫자를 입력하세요 =>'))
#num2 = 200
#print(num1 + num2)

#num1 = input()
#num1 = float(num1)
#num2 = 200
#print(num1 + num2)

#int = 정수, float = 실수

#03/14===============================================================================================================

#print("##택배를 보내기 위한 정보를 입력하세요")
#name = input("받는 사람 :")
#address = input("주소 :")
#weight = int(input("무게(g) :"))
#print(f"** 받는 사람 ==> {name}")
#print(f"** 주소 ==> {address}")
#print(f"** 배송비(g) ==> {5 * weight}원")


#lb = int(input("파운드(ib)를 입력하세요 : "))
#print(f'{lb} 파운드(ib)는 {lb * 0.453592: .5f} 킬로그램(kg) 입니다')
#kg = int(input("킬로그램(kg)를 입력하세요 : "))
#print(f'{kg} 킬로그램(kg)는 {kg * 2.204623: .5f} 파운드(lb) 입니다')


#a = 100
#b = 300
#print(a, b)
#a, b = b, a
#print(a, b)


#a = int(input("a = "))
#b = int(input("b = "))
#result = a < b
#print(result)

#03/18===============================================================================================================

#print("여행 경비 계산기")
#peo = int(input("총 인원수를 입력하세요 : "))
#hom = int(input("숙박 비용을 입력하세요 : "))
#bob = int(input("예상 식비를 입력하세요 : "))
#oth = int(input("기타 경비를 입력하세요 : "))
#total = hom + bob + oth
#t_p = total / peo
#print(f"전체 여행 경비는 {total}이며 각자 부담해야 할 금액은 {t_p} 입니다")

#var1 = 100
#print(type(var1))

#전통적인 언어들은 변수를 선언할 때 자료형도 함께 선언
#int var1 = 10;
#파이썬은 변수를 선언할 때 자료형을 선언하지 않음
#또한 같은 변수명에 여러 자료형의 값을 대입할 수 있음

#정수형(int)
#전통적인 언어들과 달리 크기 제한이 없다
#n1 = (2**1024-1)
#print(n1)
#정수 + 정수 = 정수,실수 + 실수 + 실수,정수 / 정수 = 실수

#var1 = """난생처음"""
#print(var1)
#escape character(\) => 다음에 나오는 문자가 문법적 해석에서 '탈출'

#예시)"안녕! 이라는 문구를 출력할때 문자열의 시작과 끝을 큰따옴표를 사용하면 문제가 발생
#str1 = ""\안녕!\""
#print(str1)

#str3 = '"안녕!~~~"'
#print(str3)

#msg = 'Park Seol Rin'
#print(len(msg))
#len()은 python의 built-in 함수, 문자열 뿐만아니라 리스트에도 사용 upper(),count(),find()에서도 사용함
#count() 문자열에서 어떤 글자가 몇 번 등장하는지 확인함
#어떤 글자가 어디에 있는지 알려줌
#print(msg.lower())
#print(msg.find("l"))
#문자열에서 각 문자를 가져오고 싶을 때에는 '인덱스'를 사용
#인덱스는 0부터 시작
#print(msg[6])

#03/21================================================================================================================
#if/else if/else
#if 조건1이 참이면:
# 실행할 코드
#if 조건2가 참이면:
# 실행할 코드
#else if 조건3이 참이면 :
# 실행할 코드
#else:(아무것도 해당되지 않으면)
# 실행할 코드

#if 조건을 만족할 때 실행되어야 하는 종속코드는 들여쓰기를 포함해야 된다.
#주의사항
# 1. 들여쓰기에 사용된 공백은 모두 동일하게 할 것
# 2. 종속코드와 관계없는 코드를 섞지놓지 말 것
#num = float(input('숫자를 입력하시오 ==> '))
#if num > 100:                #조건부
    #print(f'{num}은')        #종속(들여쓰기) 코드
    #print('100보다')         #종속 코드
    #print('큽니다')          #종속 코드
#else:
    #print(f'{num}은')
    #print('100보다')
    #print('작습니다')
#들여쓰기 이전 코드에 대한 종속을 의미
#print('1')
#    print('2')
#        print('3')
#    print('4')
#        print('5')
#        print('6')
#            print('7')
#    print('8')
#print('9')

#3/25=================================================================================================================
#number = int(input('숫자를 입력하시오 ==> '))
#if number >= 10:
    #if number > 10:
        #print("와! 10보다 크네요")
    #else:
        #print("흠 10보다 작네요")

#score = int(input('점수를 입력 ==> '))

#if score >= 90 :
    #print("A", end='')
#elif score >= 80:
    #print("B", end='')
#elif score >= 70:
    #print("C", end='')
#elif score >= 60:
    #print("D", end='')
#else:
    #print("F", end='')
#print('학점입니다')

#숫자 랜덤 생성
#import random #이 코드에서는 랜덤 모듈을 포함한다
#random.randint(a,b) => a에서 b까지의 숫자 중 하나를 뽑는다.
#num = random.randint(1, 45) #num = 1~45
#print(num)

#age = int(input("나이를 입력하시오 ==> "))

#if age <= 18:
    #print('얼라는 집가라!')
#else :
    #print('즐겜하세요!')
#print('협조 감사합니다')

#컴퓨터와 가위바위보 프로그램
#import random
#me = input('가위/바위/보 중에 하나를 입력하세요 ==> ')
#cpu = random.choice(['가위', '바위','보'])

#print(f'컴퓨터 : {cpu}')
#if cpu == "가위":
 #   if me == "가위":
#        print("비겼네요")
#    elif me == "바위":
#        print("이겼네요!")
#    elif me == "보":
#        print('졌네용^^ ㅎㅎ')
#elif cpu == "바위":
#    if me == "바위":
#        print("비겼네요")
#    elif me == "보":
#        print("이겼네요!")
#    elif me == "가위":
#        print('졌네용^^ ㅎㅎ')
#elif cpu == "보":
#    #if me == "보":
#        print("비겼네요")
#    elif me == "가위":
#        print("이겼네요!")
#    elif me == "바위":
#        print('졌네용^^ ㅎㅎ')

#3/28=====================================================================================================
# for 반복문
# for (변수) in (순서가 있는 데이터)
# {순서가 있는 데이터}에서 데이터를 하나씩 변수에 대입해서 사용한다 <<<
# 예시.1 기본형
#for n in [1, 2, 3]:
#    print(n)

# 예시.2 순서가 있는 데이터의 변경
#for n in [59, 22, 11, 32]:
#    print(n)

# 예시.3 변수명을 변경
#for std_no in [59, 22, 11, 32]:
#    print(f'학번 : {std_no}')

# 예시.4 파이썬에서 for문은 가져와야 하는 데이터의 갯수에 따라 반복 횟수가 결정됨
#for std_no in [1, 2, 3, 4, 5, 6, 7]:
#    print('안녕하세요 ^^')     # 4번 출럭

# 예시.5   range 객체를 이용해 반복 횟수 제어
#         range({시작값}, 끝값, {증감값})
#         range(끝값) ==> 0부터 (끝값-1) 까지의 숫자를 생성
#         range(시작값, 끝값) ==> 시작값부터 (끝값-1) 까지의 숫자를 생성
#         range(시작값, 끝값, 증감값) ==> 시작값부터 증감값을 더하면서 (끝값-1)을 넘어서지 않는 숫자를 생성
#for n in range(1, 10, 2):
#    print(n, end=' ')

#예시.6 가져온 데이터가 반복문의 실행과 연관이 없을때
#for n in range(5):                    #언더바(_)는 와일드카드(wildcard)/ 버린다는 뜻
#    print('다섯번 반복~')

#예시.7 '순서가 있는 데이터'는 모두 사용가능하다
# msg = 'AABACDEF'
# a_count = 0
# for c in msg:
#     if c == 'A':
#         a_count += 1
# print(f'A의 갯수 : {a_count}')

# for n in range(1, 11):
#     print(n, end=' ')

#range는 순서가 있는 데이터형이므로 다른 비슷한 유형인 list로 변환도 가능함
# var1 = range (1, 11) # 1 ~ 10
# my_list = list(var1)
# print(my_list)

#팩토리얼 구하는 프로그램
#팩토리얼 => 자연수 n이 주어졌을때 1부터 n까지의 곱


# n = int(input('n을 입력하시오 ==> '))
# fac = 1
#
# for num in range(1, n+1):
#     fac = fac * num
# print(f'{n}!은 {fac}입니다.')

