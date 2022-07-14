# # 조건문에서 아무 일도 하지 않게 설정하기
# pocket = ['money']

# if 'money' in pocket:
#     pass
# else:
#     print('you don\'t have money')

# print('end.')    

# 조건부 표현식(1줄로 if문 쓰기)
# score = 80
# print("success") if score >= 70 else print("failure")

# 중첩 if문(if문 안에 if문 안에 if문 안에 ....)
# a = 195

# if a > 100:
#     if a > 150:
#         print('a is bigger than 150')
#     else:
#         print(' a is bigger than 100, less than 150')
# else:
#     print('a is less than 100')


# elif
# a = 125

# if a < 100:
#     print('a is less than 100')
# elif a > 150:
#     print("a is bigger than 150")
# else:
#     print("a is bigger than 100, less than 150")

# print("end program")    

# score = int(input('성적을 입력하세요: '))

# # if score >= 90:
# #     print('a')
# # elif score >= 80:
# #     print('b')
# # elif score >= 70:
# #     print('c')    
# # elif score >= 60:
# #     print('d')
# # else:
# #     print('f')

# cut_line = [95,90,85,80,75,70,65,60,0]
# grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

# for i, v in enumerate(cut_line):
#     if score >= v:
#         print(grade[i], '학점입니다.')
#         break
    


# --------------------------------------------------

# # while문
# treeHit = 0
# while treeHit < 10:
#     treeHit += 1
#     print(f'나무를 {treeHit}번 찍었습니다.')
#     if treeHit == 10:
#         print('나무 넘어갑니다.')

#---------------------------------------------------

# a = 0

# while a < 10:
#     a = a + 1
#     if a % 2 == 0: continue # continue == 루프의 맨 처음으로 돌아간다.

#     print(a)


# i, hap = 0,0
# while i < 11:
#     hap = hap + i
    
#     i += 1

# # print("1부터 10까지의 합계: %d" % hap)

# while True:
#     print('ㅋ', end='')
#     i += 1
#     if i == 1000: break

#---------------------------------------------------

# hap = 0
# a, b = 0,0

# while True:
#     a = int(input('더할 첫번째 수를 입력하세요: '))
#     b = int(input('더할 두번째 수를 입력하세요: '))

#     if a == 0 or b == 0:
#         print('0이 입력되었습니다.')
#         break

#     hap = a+b
#     print(f"{a} + {b} = {hap}")

# from ntpath import join


# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# b = ['life','is','too','short']
# res = ' '.join(b)
# print(res)

# c = dict()
# c[(1,)] = 13

# c.pop((1,))

# d=e=[1,2]
# d[0]=3
# print(e)

# Quiz_0711
# # 1

# a, b = 0,0
# oper_list = ['+','*','-','/','%','//','**']

# while True:
#     a = int(input('계산할 첫번째 수를 입력하세요: '))
#     b = int(input('계산할 두번째 수를 입력하세요: '))
#     oper = input('계산할 연산자를 입력하세요: ')

#     if b == 0 and oper == '/':
#         break

#     if oper in oper_list:
#         print(f"{a} {oper} {b} = ", end='')
#         if oper == '+': print(a+b)
#         elif oper == '*': print(a*b)
#         elif oper == '-': print(a-b)
#         elif oper == '/': print(a/b)
#         elif oper == '%': print(a%b)
#         elif oper == '//': print(a//b)
#         elif oper == '**': print(a**b)    
#     else:
#         print('잘못된 연산자를 입력하였습니다.')    


# # 2

# tp = int(input('현재 기온을 입력하시오: '))

# if tp >= 30:
#     print('반바지를 입으세요.')
# else:
#     print('긴바지를 입으세요.')

# print('이제 나가서 운동하세요!')

# # 3

# mt = int(input('월을 입력하시오: '))
# print(f'{mt}월의 날수는 ', end=' ')

# if mt <= 0 or mt > 12:
#     print('잘못 입력하셨습니다')
# elif mt == 2:
#     print('28일')
# elif mt in (4,6,10):
#     print('30일')
# else:
#     print('31일')

# # 4
# i = 1
# while i < 10:
#     print(f'3 * {i} = {3*i}')
#     i += 1

# 5
# st = int(input('시작 값을 입력하세요: '))
# en = int(input('끝 값을 입력하세요: '))

# it = int(input('증가값을 입력하세요: '))

# num = st
# result = 0
# while num <= en:
#     result += num
#     num += it

# print(f'{st}부터 {en}까지 {it}씩 증가시킨 값의 합계: {result}')


def solution(record):
    manager = []
    dict_uid_name = {1:1}

    for i in record:
        a = i.split()
        if len(a) == 3:
            dict_uid_name[a[1]] = a[2]
        if a[0] != 'Change':
            manager.append([a[0], a[1]])


    answer = []
    for i in manager:
        answer.append(dict_uid_name[i[1]] + '님이' + ' 들어왔습니다.') if i[0] == 'Enter' else     answer.append(dict_uid_name[i[1]] + '님이' + ' 나갔습니다.')
    
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))    