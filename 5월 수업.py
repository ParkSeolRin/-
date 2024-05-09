# 05/02

# 함수 : 입력값(파라미터)을 받아 지정한 처리 결과를 계산하고 계산된 결과를 반환하는 것

# def 함수이름(파라미터1, 파라미터2, ....)
#     처리코드
#     ... 생략
#     return 반환값

# # 1. 가장 기본적인 함수(입력 X, 출력 X)
# def my_func1():
#     print("my_func1 호출")
# my_func1()
#
# # 2. 입력값이 1개 있는 경우
# def my_func2(a):
#     print(f"my_func2 호출 : {a}")
# my_func2(10)
#
# # 3. 입력값이 여러개 있는 경우
# def my_func3(num1,num2,num3):
#     res = num1 + num2 - num3
#     print(f"my_func3 호출 : {res}")
# my_func3(20,10,5)
#
# # 4. 반환값이 1개 있는 경우
# def my_func4(num1,num2,num3):
#     res = num1 + num2 - num3
#     print(f"my_func4 호출 : {res}")
#
#     return res
#
# v4 = my_func4(10,5,3)             #반드시 변수에 담을 필요 X
# print(f"v4 : {v4}")
#
# # 5. 반환값이 2개 이상인 경우
# def my_func5(num1,num2):
#     mul = num1 * num2
#     div = num1 / num2
#     print(f"두수의 곱 : {mul}, 나눗셈 : {div}")
#     return (mul, div)
#
# r1, r2 = my_func5(3,5)
# print(f"my_func5의 결과 : {r1}, {r2}")
#
# # 모든 프로그래밍 언어에서 함수는 값을 하나밖에 반환하지 못한다.=====> (O)


# 함수의 파라미터에 기본값을 설정할 수 있음
# 기본값 => 값이 지정되지 않았을 때 사용할 값
# def p2_func(v1, v2):
#     print(v1 + v2)
#
# def hap_func(v1, v2, v3):
#     print(f"{v1}, {v2}, {v3}")
#     print(v1 + v2 + v3)
#
# hap_func(1,2,3)
#
# def hap3(*nums):
#     print(nums)
#     print(type(nums))
#
# hap3(1,2)
# hap3(1,2,3,4,5)
#
# # 기본값이 있는 파라미터는 없는 파라미터보다 뒤에 작성되어야 한다.
#
# def p_func(v1,v2,v3):
#     print(sum(v1,v2,v3))
#
# p_func(v1=2,v2=3,v3=4)

# 05/09 =======================================================================================================================================

# 계산기 만드는 문제

# def clac(v1,v2,op):
#     if (op == '+'):
#         return v1 + v2
#     elif (op == '-'):
#         return v1 - v2
#     elif (op == '*'):
#         return v1 * v2
#     elif (op == '/'):
#         return v1 / v2
#
# op = input('계산입력 (+, -, *, /): ' )
# v1 = int(input('숫자 1 입력 : '))
# v2 = int(input('숫자 2 입력 : '))
# result = clac(v1, v2, op)
# print(f"계산결과 : {v1} {op} {v2} = {result}")

# List Comprehension
# 리스트를 만드는 방법 중 하나

# 빈 리스트를 만들고
# 특정규칙에 따라 결정되는 값으로
# 리스트를 채워야하는 작업에 대해서 사용
# 보통은 for문을 이용해서 리스트를 만드는 경우에 사용하는 문법

# 예) 3의 배수를 8개 갖는 리스트 선언
# my_list = []
# for x in range(1, 9):
#     my_list.append(x * 3)
# print(my_list)
#
# my_list = [x * 3 for x in range(1, 9)]
# print(my_list)

# 파이썬은 c언어 파생
# 전통적인 언어들은 함수를 정의할 때 반환값의 자료형을 써야함

# def my_func():
#     print('함수 호출')
#     return
# a = my_func
# print(a)

# def my_func():
#     print('함수 호출')
#     val = input('사용자 입력(0이면 종료) : ')
#
#     if val == 0:
#         return
#     result = val + 5
#     return result

# for i in range(1, 100):
#     if i % 2 == 0:
#         pass
#     else:
#         print(f"{i}는 홀수",end = ' ')
#
#     print('!')

# 지역변수와 전역변수
# local variable, global variable

# 종속코드는 부모(조상)코드에서 선언된 변수에 접근이 가능
# (+) 함수는 종속코드로 간주
# a = 10
# b = 20
#
# def my_func(a, b):
#     print(f"my_func : {a}, {b}")
#     c = a + b
#
# print(a,b)
# my_func(20, 30)

# a = 10
#
# def a_changer():    # 변수 a의 값을 30으로 변경하는 함수
#     global a
#     a = 30
#     print(f"a의 값 : {a}")
# a_changer()
# print(a)

# def my_func1():
#     a = 100
#
#     def my_func2(v):
#         return a + v
#     print(my_func2(30))
#
# my_func1()