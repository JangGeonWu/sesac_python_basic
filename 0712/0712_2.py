# 함수란 무엇인가?
# 입력 값을 가지고 어떤 일을 수행한 다음에 결과물을 내어놓는 것.

# def add(a, b):
#     return a+b

# print(add(3,5))

# 함수가 필요한 이유, 아래의 내용을 여러번 반복하게 해보자.
# coffee = int(input('어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)\n'))

# print('\n#1. 뜨거운 물을 준비한다.')
# print('#2. 종이컵을 준비한다.')

# if coffee == 1:
#     print('#3. 보통 커피를 탄다.')
# elif coffee == 2:
#     print('#3. 설탕커피를 탄다.')
# elif coffee == 3:
#     print('#3. 블랙커피를 탄다.')
# else:
#     print('#3. 아무거나 탄다.')

# print('#4. 물을 붓는다.'); print('끝')

# --- 함수 생성 ---

# def coffeemachine(coffee):
#     # coffee = int(input('어떤 커피를 드릴까요?(1:보통, 2:설탕, 3:블랙)\n'))

#     print('\n#1. 뜨거운 물을 준비한다.')
#     print('#2. 종이컵을 준비한다.')

#     if coffee == 1:
#         print('#3. 보통 커피를 탄다.')
#     elif coffee == 2:
#         print('#3. 설탕커피를 탄다.')
#     elif coffee == 3:
#         print('#3. 블랙커피를 탄다.')
#     else:
#         print('#3. 아무거나 탄다.')

#     print('#4. 물을 붓는다.')
#     print('#5. 스푼으로 젓는다.'); print('끝')

# coffeemachine(1)
# coffeemachine(2)
# coffeemachine(3)

# 응용
## 전역 변수 선언 부분
# coffee = 0

# ## 함수 선언 부분
# def coffee_machine(button):
#     if button == 1:
#         print('#3. 보통 커피를 탄다.')
#     elif button == 2:
#         print('#3. 설탕커피를 탄다.')
#     elif button == 3:
#         print('#3. 블랙커피를 탄다.')
#     else:
#         print('#3. 아무거나 탄다.')

#     print('#4. 물을 붓는다.')
#     print('#5. 스푼으로 젓는다.'); print('끝')

# coffee = int(input('A손님 어떤 커피를 원하시나요?'))

# coffee_machine(coffee)

# coffee = int(input('B손님 어떤 커피를 원하시나요?'))

# coffee_machine(coffee)

# -------------------------------------------
# def plus(v1, v2):
#     res = 0
#     res = v1 + v2
#     return res

# hap = 0

# hap = plus(11, 13)
# print(hap)
# -------------------------------------------

# def calc(v1, v2, op):
#     if op == '+':
#         return v1 + v2
#     elif op == '-':
#         return v1 - v2
#     elif op == '*':
#         return v1 * v2
#     elif op == '/':
#         if v2 == 0: print('0으로 나눌 수 없습니다.'); return 'err'
#         else: return v1 / v2
#     elif op == '**':
#         return v1 ** v2
#     elif op == '%':
#         return v1 % v2
#     elif op == '//':
#         return v1 // v2
#     else:
#         print("지원하지 않는 연산자입니다.")
#         print('다음 연산자만 지원합니다: +,-,*,/,%,//,**')
#         return 'err'


# oper = input('계산할 연산자를 입력하세요: ')
# var1 = int(input('첫번째 수를 입력하세요: '))
# var2 = int(input('두번째 수를 입력하세요: '))

# res = calc(var1, var2, oper)

# print(f"{var1} {oper} {var2} = {res}")


# # ---------------------------------------

# # 입력값이 없는 함수
# def say():
#     return 'hi'

# print(say())    

# 결과값(return)이 없는 함수

# def sum(a,b):
#     print(f"{a} + {b} = {a+b}")

# sum(3,5)

# 입력도 없고 결과도 없는 함수

# def sayhi():
#     print('hi~')

# sayhi()

# # ----------------------------------------

# def sum_many(*args): # parameter 앞에 '*'을 붙이면 입력값들을 전부 모아 튜플로 만들어줌
#     sum = 0
#     for i in args: # args라는 튜플을 기반으로 수행, 튜플은 값 수정 불가능한 리스트
#         sum += i
#     return sum

# result = sum_many(1,2,3,4,5,6,7,8,9,10,10)    
# print(result)

# ---------------------------------------
# 함수의 결과값은 언제나 하나이다.
# def sum_and_mul(a,b):
#     return a+b, a*b # 여러개의 값을 반환할 때에는

# result = sum_and_mul(3,9) # 튜플의 형태로 돌려준다.

# print(result)

# --------------------------------------
# 입력 인수에 따른 초깃값 미리 설정하기
# def say_myself(name, old, man=True):
#     print(f"내 이름은 {name}입니다.")
#     print(f"나이는 {old}살입니다.")
#     if man:
#         print('남자입니다.')
#     else:
#         print('여자입니다.')
#     print('')

# say_myself('김남자', 27)
# say_myself('최여자', 22, False)
# say_myself('박남자', 28, True)

# -----------------------------------------

# a = 1 # 전역변수(global variable)
# def vartest(a):
#     a += 1 # 지역변수(local variable)

# vartest(a) # 전역변수를 파라미터로 넘겼을 뿐, 전역변수는 바뀌지 않는다.
# print(a)

# -----------------------------------------
# 함수 내에서 함수 밖의 변수를 변경하는 방법 1
# a = 1 # 전역변수(global variable)
# def vartest(a):
#     a += 1 # 지역변수(local variable)
#     return a

# a = vartest(a) # 전역변수를 입력으로 한 함수의 리턴값을 대입
# print(a)

# -----------------------------------------
# 함수 내에서 함수 밖의 변수를 변경하는 방법 2, 권장되지 않음
# a = 1 # 전역변수(global variable)
# def vartest():
#     global a # 전역변수를 사용한다는 뜻
#     a += 1

# vartest()
# print(a)
# ------------------------------------------
# 전역변수와 지역변수의 이해

# def f1():
#     print(a) # 전역변수 a를 사용

# def f2():
#     a = 20
#     print(a) # 함수 내에 정의된 지역변수 a를 사용

# a = 10

# f1()
# f2()    

# -------------------------------------------
# lambda로 함수 생성하기
# lambda para1, para2, ... : parameter를 이용한 표현식
# add = lambda a, b : a+b

# print(add(3,4))

# jegob = lambda x, y : x**y

# print(jegob(2,4))

# --------------------------------------------

# Quiz-0712
# 1

def area_calc(sh_num):
    if sh_num == 1:
        wid = int(input('가로: '))
        hei = int(input('세로: '))
        print(f'면적 = {wid * hei}')
    elif sh_num == 2:
        wid = int(input('밑변: '))
        hei = int(input('높이: '))
        print(f"면적 = {wid * hei / 2}")
    else:
        rad = int(input('반지름: '))
        print("면적 = %.2f"%(rad * rad * 3.141))

area_calc(int(input('도형을 입력하시오(1: 사각형, 2:삼각형, 3: 원):')))

# 2
name_list = ['수현', '희정', '정진', '경훈']

for i in name_list:
    print(f'새싹! {i}')

# 3
text = 'I like you'
for i in range(len(text)):
    print(text[-i-1], end='')
print('')

# 4
def sum1(st, en):
    result = 0
    for i in range( st, en + 1):
        result += i
    return result

print(sum1(1,10))
print(sum1(1,50))

# 5
def exp1(a, b):
    return a**b

print(exp1(10, 2))    

# 6

def coffeemachine(customer):

    coffee = int(input(f'{customer}씨, 어떤 커피 드릴까요?(1:아메리카노/2:카페라떼/3:카푸치노/4:에스프레소)'))
    print('\n#1. 뜨거운 물을 준비한다.')
    print('#2. 종이컵을 준비한다.')

    if coffee == 1:
        print('#3. 아메리카노를 탄다.')
    elif coffee == 2:
        print('#3. 카페라떼를 탄다.')
    elif coffee == 3:
        print('#3. 카푸치노를 탄다.')
    elif coffee == 4:
        print('#3. 에스프레소 탄다.')
    else:
        print("잘못 입력하셨습니다.")
        return 0

    print('#4. 물을 붓는다.')
    print('#5. 스푼으로 젓는다.')
    print(f"{customer}씨~ 커피 여기 있습니다.\n")
    return 0

customer_list = ['혜선', '세찬', '소영', '민희']
for i in customer_list:
    coffeemachine(i)