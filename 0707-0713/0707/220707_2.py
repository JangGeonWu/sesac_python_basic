# # 산술 연산을 하는 문자열과 숫자의 상호 변환
# s1 = "100"
# s2, s3 = "200", "300" # s1 s2 s3 모두 문자열

# print(s1 + s2 + s3) # 문자열이라 concatenation 발생
# print(int(s1) + int(s2) + int(s3))

# s4 = 123.123
# print(int(s4), float(s4)) # int = 정수, float = 실수

# # 대입 연산자: +=, -=, /=, *=, %=, **=, //=
# # 파이썬에는 ++나 --같은 증감 연산자가 없다
# a = 10
# # a %= 3
# # a **= 2
# # a //= 3
# a /= 3
# print(a)

# ## 변수 선언 부분 ##
# money, c500, c100, c50, c10 = 0,0,0,0,0

# ## 교환할 돈은 얼마? ##
# money = int(input("교환할 돈은 얼마? "))

# ## 동전 교환 시스템 ##

# c500 = money // 500
# money %= 500

# c100 = money // 100
# money %= 100

# c50 = money // 50
# money %= 50

# c10 = money // 10
# money %= 10

# ## 결과 print ##
# print(f"교환 결과:\n500원 {c500}개\n100원 {c100}개\n50원 {c50}개\n10원 {c10}개")

# if money != 0: print(f"교환하지 못한 돈 {money}원이 있어요")
#--------------------------------------------------------------------------------------
# 문자열 자체 함수
# a = "hobby"
# print(a.count('b')) # count 함수 내의 문자열의 개수를 파악한다.

# print(a.find('b')) # count 함수 내의 문자열의 '첫번째'위치를 파악한다.
# print(a.find('j')) # 해당 문자열이 없으면 -1을 출력한다

# print(a.join('12345')) # 문자마다 문자열 'a'를 삽입시킨다. 즉 1->a->2->a->3->a->4->a->5 형식으로 출력한다.

# print(a.upper()) # 대문자로 전환. lower는 소문자로 변환

# b = '    lego      '
# print(b.strip()) # 양쪽의 '공백'을 제거한다.

# c = '------line--------'
# print(c.strip('-')) # 양쪽의 '-'을 제거한다.
# print(c.rstrip('-')) # 오른쪽(right)의 '-'을 제거한다.
# print(c.lstrip('-')) # 왼쪽(left)의 '-'을 제거한다.

# d = "first second third fifth"
# print(d.replace("fifth", "fourth")) # 출력할 '때'만 문자열을 바꾼다.
# print(d) # 실제 값은 바꾸지 않는다

# print(d.split()) # '공백'을 기준으로 분할한다

# e = d.replace(' ', ':')
# print(e)
# print(e.split(':')) # ':'을 기준으로 분할한다
# --------------------------------------------------------------------------------
# LIST 자료형
ODD = [1,3,5,7,9]
print(ODD)

listA = [1, 2, 3, ['a', ['b', 'c', 'd']]] # list 내부에 list 자료형을 넣을 수 있다.
print(listA)

# 리스트의 인덱싱
print(ODD[2])
print(ODD[-2])
print(ODD[2:])
print(ODD[:-2])

print(listA[-1][1][0]) # list 속에 list 속에 list...

listA[0] = 'hi' # 값 수정
print(listA)

# [] 사용해서 리스트 요소 삭제하기
ODD[1:3] = [] # ODD[1], ODD[2]인 3, 5가 삭제된다.
print(ODD) # ODD = [1,7,9]

del ODD[1] # ODD[1] = 7
print(ODD)

# 추가 append()
ODD.append(11)
print(ODD)

ODD.append([15, 19])
print(ODD)

# 정렬 sort()
k = [1,8,2,65,31]
k.sort()
print(k)

l = ['e','y','i','x','j']
l.sort()
print(l)

# 뒤집기 reverse()
l.reverse()
print(l)
# 위치 반환 index()
print(l.index('e'))

# 리스트 요소 삽입 insert(a,b), append는 그냥 뒤에 붙이고, insert는 정확한 위치를 집어 값을 삽입
l.insert(0, 'a')
print(l)

# 리스트 요소 제거 remove(x), '처음 나오는' x를 삭제
l.remove('x')
print(l)

# 리스트 요소 끄집어내기 pop(), 맨 마지막 요소를 '돌려준다'는게 중요. 물론 꺼내진 요소는 리스트에서 삭제된다.
poped = l.pop()
print('poped: '+ poped + ', l:',l)

# pop(x)는 x번째 요소를 '돌려준다'
poped = l.pop(1)
print('poped: '+ poped + ', l:',l)

# extend(x), 리스트 확장, x에는 리스트만 올 수 있다.
l.extend(['p','k'])
print(l)