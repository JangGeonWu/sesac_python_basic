# 튜플은 ( )로 둘러쌈, 리스트와 다르게 값 변경 불가능
# 튜플은 1개의 요소만을 가질 때는 요소 뒤에 콤마를 반드시 붙여줘야 함
# t2  = (1,)
# # 괄호를 생략해도 무방하다.
# t3 = 1, 2, 3

# # print(t2, t3)

# # -------------------------------------------------------------
# t1 = ()
# t2 = (1,)
# t3 = (1, 2, 3)
# t4 = 1, 2, 3
# t5 = ('a', 'b', ('ab', 'cd'))

# # print(t1, t2, t3, t4, t5)

# # ------------------------------------------------------------
# # tuple은 값 삭제 불가능
# # del t3[1] -- TypeError: 'tuple' object doesn't support item deletion

# # 값 변경도 불가능 
# # t3[1] = 4 -- TypeError: 'tuple' object does not support item assignment

# # ------------------------------------------------------------
# # 인덱싱, 슬라이싱은 가능
# print('indexing:', t3[1])
# print('slicing:',t3[1:])

# # 튜플에 값을 추가하는(더하는) 방법은 아래와 같다.
# t6 = (4,)
# t7 = t3 + t6
# print(t7)

# # 튜플에 정수형을 곱하여 반복할 수 있다,
# t8 = t3 * 3
# print(t8)

# # len function으로 튜플의 길이를 구할 수 있다.
# print(len(t8))

# ------------------------------------------------------------
# # Dictionary(딕셔너리) 자료형
# # 대응 관계를 나타내는 자료형으로, 키와 값(value)의 짝으로 구성되어진다

# dic1 = {'name':'penny', 'phone' : '01012345678', 'birth':'1118'}
# print(dic1)

# # 딕셔너리에 쌍(key: value) 추가하기
# dic1['listD'] = [1, 2, 3, 4] # key 값과 해당되는 value를 입력하면 된다.
# print(dic1)

# # 딕셔너리에서 값 삭제하기
# del dic1['birth'] # 해당되는 key값을 입력하여 삭제
# print(dic1)

# # ------------------------------------------------------------
# # 키 값을 입력해 값 얻기
# print(dic1['name'])

# # 중복되는 key값을 입력하면, 하나 이외의 나머지 짝이 전부 무시된다.
# dic2 = {1:'a', 1:'b', 1:'c', 1:'d', 1:'f', 1:'e'}
# print(dic2[1]) # 가장 뒤에 있는 key의 value만 출력한다.


# # ------------------------------------------------------------
# # 키 리스트 만들기, dict.keys() 함수는 딕셔너리 dict의 키만을 모아서 dict_keys 객체를 돌려준다.
# dic_key = dic1.keys()
# print(dic_key)
# # 중요한 것! dick_keys 객체는 indexing 기능을 제공하지 않는다. 아래의 코드는 에러를 발생시킨다. (리스트 변환에 의해 발생하는 메모리 낭비를 방지하기 위함)
# # print(dic_key[1]) -- TypeError: 'dict_keys' object does not support indexing
# # 리스트로 만들고 싶다면 list함수를 사용하면 된다.
# key_list = list(dic_key)
# print(key_list[0], key_list[1], key_list[2])

# # 근데 for문에서는 또 사용이 가능하다... 따로 for문과 dict_keys 객체에 대응되는 코드가 구현되어 있는 듯 하다.
# for k in dic1.keys():
#     print(k)

# # ------------------------------------------------------------
# # 값 리스트 만들기. dict_keys 객체와 유사하다.
# dic_value = dic1.values()
# print(dic_value)

# # 키-값 형태의 리스트 만들기. enumerate처럼 인덱스(키)와 Value가 동시에 필요한 경우에 쓰인다.
# dic_item = dic1.items()
# print(dic_item)

# # clear로 딕셔너리 비우기
# dic2.clear()
# print(dic2)

# # Key로 Value 얻기, a['name']과 다르게 '근본 없는 키'를 입력했을 때, 에러 대신 'None'을 되돌려준다는 장점이 있다.
# print(dic1.get('name'))
# print(dic1.get('name1'))
# print(dic1.get('name1', 'default_value')) # 키 값이 없을 때, None 대신 정해둔 디폴트 값을 출력하도록 할 수도 있다.

# # 해당 키가 딕셔너리 안에 있는 지 조사하기
# print('name' in dic1) # True, False로 출력한다.

# # value로 key 값을 알아낼 수는 없나요? -> key는 중복이 안되지만 value는 중복이 가능해서, .values, .items를 이용해 직접 구해야 한다.
# ------------------------------------------------------------

# Quiz1
# # 1.
# student = {'학번' : 1000, '이름': '김새싹', '학과':'컴퓨터학과'}
# print(student)

# # 2.
# student['연락처'] = '01012345678'
# print(student)

# # 3.
# student['학과'] = '전자공학과'
# print(student)

# # 4.
# print(student.get('학과'))

# # 5.
# print(student.keys())

# # 6.
# myT = (10,20,30)

# myT = myT + (40,)

# print(myT)

# ------------------------------------------------------------
# 집합 자료형, 교집합-합집합-차집합 등 집합 관련된 내용을 처리하기 위해 사용됨
# 혹은, (코딩 테스트에서) 리스트 -> 셋 -> 리스트 변환을 통해 중복된 값들을 제거하는 데 쓰인다.
# s1 = set([-1, 0, 1,2,3])
# print(s1)

# s2 = set([2,4,1,2,3,2,1,-2])
# print(s2) # 중복된 값을 허용하지 않으며, 순서가 없다. 따라서, 인덱싱으로 값을 찾을 수 없다.

# # 교집합 &, intersection
# print('intersection:',s1 & s2, end=' ')
# print(s1.intersection(s2))

# # 합집합 |, union
# print('union:',s1 | s2,end=' ')
# print(s1.union(s2))

# # 차집합 -, difference
# print('difference (s1 - s2):', s1 - s2, s1.difference(s2))
# print('difference (s2 - s1):', s2 - s1, s2.difference(s1))

# -----------------------------------------------------------
# # 값 1개 추가(add), 여러개 추가(update), 제거하기(remove)
# s1.add('a')
# print(s1)

# s1.update('b','c','d') # = s1.update(['b','c','d'])
# print(s1)

# s1.remove('c')
# print(s1)

# -----------------------------------------------------------
# 불(Bool) 자료형, True or False
# print(type(False)) # <class 'bool'>

# a = [1,2,3,4] # pop되면서 a는 빈 리스트가 된다 -> while문의 조건이 False가 되어 루프 탈출
# while a:
#     v = a.pop()
#     print(v)

# -----------------------------------------------------------
# 변수의 메모리 주소 확인하기
# a = [1,2]
# b = a

# print('id_of_a:',id(a),'id_of_b:', id(b))

# c = [3,4,5]

# print('id_of_c:',id(c),'id_of_c[0]:', id(c[0]))

# a[1] = 4
# print('a:', a,'b:', b) # b와 a가 가리키는 주소가 같기 때문.

# # 주소는 다르게, 값만 복사하고 싶다면? 리스트의 경우에는 [:]을, 다양한 경우에는 copy 모듈을 사용한다.
# b = a[:]
# a[1] = 5
# print('id_of_a:',id(a),'id_of_b:', id(b))
# print('a:', a,'b:', b) # b와 a가 가리키는 주소가 다르기 때문

# from copy import copy as cp
# c = cp(a)
# a[1] = 6
# print('id_of_a:',id(a),'id_of_c:', id(c))
# print('a:', a,'c:', c) # c와 a가 가리키는 주소가 다르기 때문

# -----------------------------------------------------------
# 여러 개의 변수를 정의하는 다양한 방법
# a1, a2 = ('tup1', 'tup2')
# print(a1, a2)
# (b1, b2) = 'tuple1', 'tuple2'
# print(b1, b2)
# [c1, c2] = ['list1', 'list2']
# print(c1, c2)
# d1 = d2 = 'value'
# print(d1, d2)
# e1, e2 = ('v1', 'v2')
# print(e1, e2)
# e1, e2 = e2, e1 # 변수 값 변환
# print(e1, e2)

# -----------------------------------------------------------
# if문, 들여쓰기를 잘 하자(IndentationError)

# money = 2000
# if money >= 3000:
#     print('택시를 타고 가라')
# else:
#     print('걸어 가라')

# pocket = ['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     print('택시를 타고 가라')
# else:
#     print('걸어 가라')


# Quiz2

# 1
# age = int(input('Tell me your age?'))

# if age < 30:
#     print('Welcome to the Club.\n')
# else:
#     print('Oh! no. You are not accepted.\n')

# 2
# num = int(input('정수를 입력하세요: '))

# if num % 2 == 1:
#     print('홀수를 입력했군요.\n')
# else:
#     print('짝수를 입력했군요.\n')

# -----------------------------------------------------------
# 3. 주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고가라는 문장을 조건문으로 만들어보자
# pocket = ['dust']

# if 'card' not in pocket:
#     print('걸어 가라')
# else:
#     print('버스를 타고 가라')

# 4. 10만원을 초과한 금액에 대해 5% 할인해주고 있습니다. 총 금액이 11만원일 경우 아래와 같은 프로그램을 작성해보세요
'''
==========result===========
구입 금액을 입력하시오: 110000
지불 금액은 104500.0입니다.
'''
price  = int(input('구입 금액을 입력하시오: '))

if price > 100000:
    price = price * 0.95

print(f"지불 금액은 {price}입니다.")





