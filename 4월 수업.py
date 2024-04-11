#04/04

#합 구하기

# i = 0
# hap = 0
# for i in range(1, 11, 1) :
#     hap = hap + i
#
# print('1에서 10까지의 합 : ', hap)

#홀수 합 구하기

# i, hap = 0, 0  <== 파이썬에서만 가능
#
# for i in range(1001, 2000, 2) :
#     hap += i
# print('1000에서 2000까지의 홀수의 합 : ', hap)

# i, hap = 0, 0
#
# for i in range(1000, 2000) :
#     if i % 2 == 1 :
#         hap = hap + i
#
# print(f'1000부터 2000까지의 홀수 합 : {hap}')

#for문 안에 for문을 사용할 수 있음
#중첩 for문이라고 함

# 구구단 계산기
# dan = 2
# for dan in range(2, 10) :
#     print(f'===={dan}단====')
#     for y in range(1, 10) :
#         print(f'{dan} * {y} = {dan * y}')

# for문: 반복할 횟수를 range()에서 결정한 후에, 그 횟수만큼 출력함
# while문: 반복 횟수를 결정하기보단 참,거짓으로 판별해 반복함

# i = 0
# while i < 3:
#     print('안녕')
#     i += 1

# 무한 반복
# i = 0
# while True:
#     print('~~')

# 무한 계산기
# while True:
#     num1 = int(input('숫자 1 입력 : '))
#     num2 = int(input('숫자 2 입력 : '))
#     print(f'{num1} + {num2} = {num1 + num2}')

#계산기
# while True:
#     num1 = int(input('숫자 1 입력 : '))
#     num2 = int(input('숫자 2 입력 : '))
#     print(f'{num1} + {num2} = {num1 + num2}')

    #break는 for, while 같은 반복문에서만 사용
    #예외적으로 switch문에서도 사용
    #break를 만나면 반복문이 종료됨
    # if num1 == 0:
    #     break

# dan = 2
# for dan in range(2, 10) :
#     print(f'===={dan}단====')
#     for y in range(1, 10) :
#         print(f'{dan} * {y} = {dan * y}')
#
#     if dan == 5:
#         break

# continue : 종속코드 블럭의 마지막으로 이동

# for i in range(5):
#     print(i, 1)
#     print(i, 2)
#     continue
#     print(i, 3)
#     print(i, 4)

# while True:
#     i += 1
#     print(i, 1)
#     print(i, 2)
#     continue
#     print(i, 3)
#     print(i, 4)

#짝수단 출력
# dan = 2
# for dan in range(2, 10) :
#     if dan % 2 == 1:
#         continue
#     print(f'===={dan}단====')
#     for y in range(1, 10) :
#         print(f'{dan} * {y} = {dan * y}')

# import random
# roll_count = 0
# while True:
#     d1 = random.randint(1, 6)
#     d2 = random.randint(1, 6)
#     d3 = random.randint(1, 6)
#     d4 = random.randint(1, 6)
#
#     roll_count += 1
#     if d1 == d2 and d2 == d3 and d3 == d4:
#         print(f'주사위는 {d1}입니다')
#         print(f'주사위를 던진 횟수는 {roll_count}입니다')
#         break

# 원주율 계산

# r = 3
# n = 2
# sign = 1
# for _ in range(20):
#     mul = 1
#     for i in range(n, n+3):
#         print(i, end = ' ')
#         mul = mul * i
#     print(f'곱 : {mul}')
#     r += 4 / mul
#     print(f'결과 : {r}')
#     n = n + 2
#     sign = -sign

# 04/08===================================================================================================

# #리스트는 대괄호로 선언
# my_list = []             # 대괄호를 이용한 빈 리스트 생성
# my_list2 = list()        # 클래스 생성자 호출을 이용한 빈 리스트 생성
# # 값과 함께 리스트 선언
# fruits = ['apple', 'pear', 'grape']
#
# #출력
# print(fruits)
# for f in fruits :
#     print(f)
#
# # 인덱스를 이용한 접근
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# 숫자 4개 입력 받은 후 합 계산
# numlist = [0, 0, 0, 0]
# hap = 0
#
# numlist[0] = int(input('숫자 = '))
# numlist[1] = int(input('숫자 = '))
# numlist[2] = int(input('숫자 = '))
# numlist[3] = int(input('숫자 = '))

# hap = numlist[0] + numlist[1] + numlist[2] + numlist[3]
# print('합계 ==> ', hap)

#숫자 4개 입력 받은 후 합 계산(for문 이용)
# numlist = [0, 0, 0, 0]
# hap = 0
#
# print(len(numlist))
#
# for n in range(4) :
#     numlist[n] = int(input('숫자 입력 ==> '))
#
# print(numlist)
#
# for n in range(4) :
#     hap += numlist[n]
# print(hap)
#
# 리스트의 모든 데이터를 인덱스를 이용해 순차적으로 접근 할때엔
# range(len(리스트)) 를 많이 이용함
#
# for n in range(len(numlist)) :
#     numlist[n] = int(input('숫자 입력 ==> '))
#
# print(numlist)

# my_list = []
# print(f'초기 리스트 : {my_list}')
# (1) append(값) : 값을 리스트의 마지막에 추가한다
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(f'append 이후 ==> {my_list}')

# my_list = [24, 54 , 32, 16]
#
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
#
# print('-----------')
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])
#
# msg = 'hello'
# print(msg[-1])

# 슬라이싱(Slicing)에 대한 내용
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 리스트[시작인덱스 : 끝인덱스] => 시작인덱스 ~ (끝인덱스-1)까지의 값을 복사
# new_list1 = my_list[2:7]
# print(new_list1)
# new_list2 = my_list[5:6]
# print(new_list2)
# new_list3 = my_list[5:5]
# print(new_list3)
#
# 시작인덱스를 생략하면 인덱스 0부터 끝인덱스-1 까지
# new_list4 = my_list[:5]
# print(new_list4)
#
# 끝인덱스를 생략하면 시작인덱스부터 리스트 끝까지
# new_list5 = my_list[5:]
# print(new_list5)
#
# 시작인덱스와 끝인덱스 둘다 생략할 수 있음
# 복사체(copy)가 만들어진다고 볼 수 있음
# 원본과 복사체가 서로 영향을 주지 않는 하드카피(Hardcopy)
# new_list6 = my_list[:]
# print(new_list6)

# 04/11 ==================================================================================================

# 음식점의 주문 관리 시스템
#
# 각각의 인덱스는 음식의 고유 코드를 나타냅니다: 0:깁밥, 1:라면, 2:돈까스, 3:샐러드
# 총매출 / 가장 많이 팔린 음식, 횟수
# food_price = [1200, 1500, 1800, 1000]
# order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]
#
# total = 0
# order_cnt = [0] * len(food_price)
#
# for order in order_history :
#     total += food_price[order]
#     order_cnt[order] += 1
#
# 가장 많이 팔린 횟수
# max_cnt = 0
# for c in order_cnt :
#     if c > max_cnt :
#         max_cnt = c
# print(f'총가격 : {total}')
#
# food_name = ['김밥', '라면', '돈까스', '샐러드']
# for idx in range(len(order_cnt)) :
#     if order_cnt[idx] == max_cnt :
#         print('가장 많이 팔린 음식 :', food_name[idx])
#
# print(f'{max_cnt}회')

# 특정 위치의 값 변경
# num_list = [10, 20, 30]
# num_list[1] = 200
# print(num_list)
# print(f'num_list의 길이 : {len(num_list)}')
#
# 일정 범위의 값 변경 (슬라이싱 이용)
# num_list = [10, 20, 30]
# num_list[1 : 2] = [200, 201]
# print(num_list)
# print(f'num_list의 길이 : {len(num_list)}')

# num_list = [10, 20, 30]
# num_list[1] = [200, 201]
# print(num_list)
# print(f'num_list의 길이 : {len(num_list)}')

# 리스트에 값을 추가
# append(값) : 리스트의 제일 뒤에 있는 값을 추가한다.
# insert(인덱스, 값) : 인덱스 위치에 값을 추가하고 기존의 값들을 뒤로 민다.

# 리스트에 있는 값을 삭제
# (1) del을 이용하는 방법
#     del(리스트) 또는 del(리스트[인덱스])
#     del은 List의 함수가 아님.파이썬의 기본 내장 함수
#     del은 선언되어있는 객체를 삭제하는 기능을 가짐
#     remove는 값을 삭제하는 대신
#     del은 인덱스를 이용하여 값을 삭제 할 수 있음

# num_list = [10, 20, 30]
# del num_list[1]
# print(num_list)
#
# # (2) remove(값)을 이용하는 방법
# #       주의 할 점: 값이 여러개 잇으면 제일 앞에 있는 것만 지워짐
# num_list = [10, 20, 30, 20, 10]
# num_list.remove(20)
# print(f'remove를 이용한 삭제 : {num_list}')
#
# for _ in range(num_list.count(20)) :
#     num_list.remove(20)
# print(f'반복문과 remove를 이용한 삭제 : {num_list}')
#
# if 55 in num_list :    #55가 num_list에 있으면 지워라
#     num_list.remove(55)
#     print(num_list)
#
# print(num_list.count(55))
#
# num_list.pop()
# print(num_list)
#
# # 정렬 (sort) - 리스트의 함수
# num_list = [20, 40, 1, 12, 55]
# num_list.sort()
# print(num_list)
# num_list.sort(reverse = True)
# print(num_list)
#
# #정렬 (sorted) - 파이썬의 기본 함수
# num_list = [20, 40, 1, 12, 55]
# num_list2 = sorted(num_list)
# print(num_list)
# print(num_list2)
#
# # 문자열도 사전순으로 정리 가능
# str_list = ['다람쥐', '가구', '바나나', '사자']
# str_list.sort()
# print(str_list)
#
#
# # 리스트를 역순으로 만들기
# num_list = [10, 20, 30]
# num_list.reverse()
# print(num_list)
#
# # 리스트 복사
# num_list = [10, 20, 30]
# num_list = num_list2 # <== 얕은 복사 : 두 변수가 같은 객체
# num_list2[1] = 200
# print(f'num-list : {num_list}')
# print(f'num_list2 : {num_list2}')
#
# num_list = [10, 20, 30]
# num_list2 = num_list.copy() # <== 깊은 복사 : 두 변수가 독립적
# num_list2[1] = 200
# print(f'num-list : {num_list}')
# print(f'num_list2 : {num_list2}')