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

# 05/16 =================================================================================================================================

# # y와 p의 개수가 동일한지?
# # 1) 대소문자를 구별하지 않는다
#
# def solution(msg):
#     msg = msg.lower()
#     p_count = msg.count('p')
#     y_count = msg.count('y')
#
#     if p_count == y_count:
#         return True
#     else:
#         return False
#
# s = 'pPoooyY'
# print(solution(s))
# s = 'Pyy'
# print(solution(s))

# 하샤드 수 : 각 자릿수를 더한 값으로 나누었을 때 나머지가 0이면 True,아니면 False   ==================================

# def solution(n):
    # 각 자릿수 합
    #  1. 수학적으로
    # hap = 0
    # tmp = n
    # while n != 0:
    #     hap += tmp % 10        # 1의 자릿수 누적
    #     tmp = tmp / 10           # 1의 자릿수 버림

    # 2. 문자열 변환으로
    # 리스트의 요소들에게 각각 특정 함수를 씌우는 방법
    # map 함수    map(함수, 리스트)
    # map 함수의 결과는 map 객체
    # return n % sum(list(map(int,list(str(n))))) == 0  <=== 짧게 하기

    # hap = 0
    # msg= str(n) # int to string
    # l = list(msg)  # string to list
    #
    # for c in l:
    #     hap += int(c)
    #
    #
    # if n % hap == 0:
    #     return True
    # else:
    #     return False

# arr = [10, 12, 11, 13]
# for n in arr:
#     print(solution(n))

# 정수 내림차순 배치 ==========================================================================================
# def soltuion(num):
#     nl = list(str(num))
#     nl.sort(reverse = True)
#     print(nl)
#
#     list to string
#     msg = ''
#     for n in nl:
#         msg += n
#     # string to int
#
#     # 구분문자열.join(문자열 리스트)
#     # => 문자열(구분문자열)문자열(구분문자열)....
#     msg = ''.join(nl)
#
#     result = int(msg)
#     return result
# n = 118372
# print(soltuion(n))

# X만큼 간격이 있는 n개의 숫자 =========================================================================================================
# X부터 X씩 증가하는 숫자 n개가 담긴 리스트를 변환
# def solution(x, n):
#     nl = []
#     for i in range(1, n+1):
#         nl.append(x * i)
#     return nl
#
# x_list = [2, 4, -4]
# n_list = [5, 3, 2]
#
# for i in range(len(x_list)):
#     print(solution(x_list[i], n_list[i]))     # 방법 1
#
# for x, n in zip(x_list, n_list):
#     print(solution(x, n))                  # 방법 2

# 두 정수 사이의 합 ==========================================================================
# def solution(a, b):
#     if a > b:
#         a, b = b, a
#
#     # 삼항연산자(Tri-op)
#     # 변수 = 참일때 값 if 조건식 else 거짓일 때 값
#
#     a, b = b, a if a > b else a, b
# 
#     hap = 0
#     for i in range(a, b + 1):
#         hap += i
#     return hap
#
#     hap = sum(list(range(a, b+ 1)))
#     return hap
#
# a_list = [3, 3, 5]
# b_list = [5, 3, 3]
#
# for a, b in zip(a_list, b_list):
#     print(solution(a, b))

# 05/23 =====================================================================================================================================

# 11.정수 n, m이 주어졌을 때 가로 n X 세로 m 의 형태로 직사각형 모양의 '*' 출력
# # Solution-1
# def solution(n, m):
#     for _ in range(m):
#         for _ in range(n):
#             print('*', end = '')
#         print('')
#
# solution(5,3)

# # Solution-2.
# def solution(n, m):
#     for _ in range(m):
#         print('*' * n)
#
# solution(5,3)

# 12. 문자열 s를 입력받아 가운데 글자를 출력 s의 길이가 홀수면 가운데 글자 하나만 반환, 짝수면 가운데 글자 2개를 반환

# # Solution-1
# def solution(s):
#     if len(s) % 2 != 0:
#         return s[len(s) // 2]
#     else:
#         return s[len(s) // 2 - 1] + s[len(s) // 2]
#
#
# s = 'abcde' # 'c'    len(s) // 2
# print(solution(s))
# s = 'qwer' # 'we'    len(s) -> 4      len(s) // 2 - 1, len(s) // 2  => 2
# print(solution(s))

# 13. 두 행렬의 합
# def solution(arr1, arr2):
#     y, x = len(arr1), len(arr1[0])
#     result = []
#     for _ in range(y):
#         row = [0] * x
#         result.append(row)
#
#     for row in range(y):
#         for col in range(x):
#             result[row][col] = arr1[row][col] + arr2[row][col]
#     return result

# 14. 내적
# a와 b의 내적 -> 컨블루션 연산

# # Solution-1
# def solution(a, b):
#     result = 0
#     for idx in range(len(a)):
#         result += a[idx] * b[idx]
#     return result

# a = [1, 2, 3, 4]
# b = [-3, -1, 0, 2]
# print(solution(a, b))
#
# a = [-1, 0, 1]
# b = [1, 0, -1]
# print(solution(a, b))


# # Solution-2
# def solution(a, b):
#     result = 0
#     for idx in range(len(a)):
#         result += a[idx] * b[idx]
#
#     result = sum(a[idx] * b[idx] for idx in range(len(a)))
#     return result
#
# a = [1, 2, 3, 4]
# b = [-3, -1, 0, 2]
# print(solution(a, b))
#
# a = [-1, 0, 1]
# b = [1, 0, -1]
# print(solution(a, b))

# 15. 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인
# def solution(s):
# # Solution-1
    # if len(s) == 4 or len(s) == 6:
    #     return s.isdigit()  # 문자열 s가 숫자인가?
    # else:
    #     return False


# # Solution-2
#     return True if (len(s) == 4 or len(s) == 6) and s.isdigit() else False
#
# s = 'a234'
# print(solution(s))
# s = '1234'
# print(solution(s))
# s = '12345'
# print(solution(s))

# 16. 연속적으로 나타나는 같은 숫자 제거

# arr = [1,1,3,3,0,1,1]
# 기준 arr[0] ==> 1

# arr[0]과 arr[1]을 비교 ==> 1, 1 ==> 같은 숫자
# arr[1] 삭제

# 기준 arr[0] ==> 1
# arr[0]과 arr[1]을 비교 ==> 1, 3 ==> 다른 숫자

# len(arr) - 1 까지 While문으로 반복
# ====================================================
# arr = [1,1,3,3,0,1,1]
# for문을 이용해서 len(arr) - 1까지 순회
# visited => 마지막으로 관찰된 숫자
# 현재 관찰중인 숫자 != visited ? 다르면 result 리스트에 추가

# def solution(arr):
#     visited = arr[0]
#     result = []
#     for idx in range(1, len(arr)):
#         if arr[idx] != visited:
#             result.append(visited)
#         visited = arr[idx]
#
#     if result[-1] != visited:
#         result.append(visited)
#     return result
#
#
# arr = [1,1,3,3,0,1,1]
# print(solution(arr))
# arr = [4,4,4,3,3]
# print(solution(arr))


# 17.
# 각 단어의 짝수번째 인덱스 문자를 대문자
#         홀수번째 인덱스 문자를 소문자

# def solution(s):
#     # 문자열.split(구분자)  => 구분자를 기준으로 문자열을 나눈다
#     words = s.split(' ')
#     for w_idx in range(len(words)):
#         word = ''
#         for c_idx in range(len(words[w_idx])):
#             if c_idx % 2 == 0:
#                 word += words[w_idx][c_idx].upper()
#             else:
#                 word += words[w_idx][c_idx].lower()
#         words[w_idx] = word
#
#     result = ' '.join(words)
#     return result
#
# s = "try hello world"
# print(solution(s))

# 05/27 ==================================================================================================================================

# fp = open('input.txt', 'r', encoding= "UTF-8")
# msg = fp.readline().strip()  # .strip() => 문자열의 함수, 마지막에 있는 엔터값을 없애줌
# print(msg)
# msg = fp.readline().strip()
# print(msg)
# msg = fp.readline().strip()
# print(msg)
# msg = fp.readline().strip()
# print(msg)
# fp.close()  # 파일 닫기
#
# fp = open('input.txt', 'r', encoding= "UTF-8")
# while True:
#     msg = fp.readline().strip()
#     if msg == '':
#         break
#     print(msg.strip())
#
# fp = open('input.txt', 'r', encoding= "UTF-8")
# msg_list = [m.strip() for m in fp.readlines()]
#
# # for 인덱스, 값 in enumerate(순서가 있는 데이터)
# # enumerate는 인덱스와 값을 묶은 정보를 만들어줌
#
# for idx, msg in enumerate(msg_list):
#     print(f'{idx+1} : {msg}')
#
# for msg in msg_list:
#     print(msg)
# fp.close()

# write(문자열) - 문자열을 파일에 쓴다
# write(문자열) - 문자열 + 개행문자를 파일에 쓴다
# wrtie(문자열 리스트) - 리스트에 있는 문자열을 한 줄씩 파일에 쓴다

# fp = open('output.txt', 'w')
# fp.write('안녕')
# fp.write('하세요\n')
# fp.write

# open(파일 경로, 모드, encoding = 'UTF - 8')
# 모드 => 'r': 읽기, 'w':'쓰기', 'a': '추가'
#        'w' 또는 'a'모드로 열린 파일은 닫을 때까지
#        다른 프로그램이 사용할 수 없음(트랜젝션 : Transaction)

# readline() : 한줄 읽기
# readlines() : 모든 줄을 읽어서 리스트에 담기
#    (+) 문자열의 strip():문자열 끝에 있는 엔터값(개행문자)을 없애줌

# 18.
# 가지고 있는 돈 money에 대해서 price원인 놀이기구를 count번 탈려고 할 때
# 얼마가 부족한가?
# 이 때, 놀이기구는 탈 때마다 price만큼 비싸진다
# def solution(price, money, count):
#     cost = sum([price * x for x in range(1, count + 1)])
#     return max(0, cost - money)
#
# print(solution(3, 20, 4))
