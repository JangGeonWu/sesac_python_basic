# input : 입력되는 모든 것을 문자열로 취급한다
# a = input()

# print(a)
# print(type(a))

# number = input('enter the number:')
# print(number)
# print(type(number))

# k = input().split()
# print(k)

# --------------------------------------------
# 파일 생성
# f = open("./0713/myfile2.txt", 'w')

# f.close

# --------------------------------------------
# 파일 생성 후 출력값 적기
# f = open("./0713/myfile.txt", 'w')
# for i in range(1, 11):
#     data = '%d line.\n'%i
#     f.write(data) # 기존 파일의 내용이 지워지고 'data' 값을 입력함

# f.close()
# -------------------------------------------
# 파일 읽는 방법 : readline
# f = open("./0713/myfile.txt", 'r')
# line = f.readline() # 파일의 라인 하나를 불러온다
# print(line) # line 하나를 불러와 화면에 출력

# while True:
#     line0 = f.readline() # 위에서 readline을 호출해서 2번째 line부터 읽음
#     if not line0: break
#     print(line0)

# f.close()
# -----------------------------------------
# 파일 읽는 방법2 : readlines()
# f = open("./0713/myfile.txt", 'r')
# lines = f.readlines() # 파일의 라인을 모두 읽어 리스트의 형태로 저장한다.
# for l in lines:
#     print(l)

# f.close()
# -----------------------------------------
# 파일 읽는 방법3 : read()
# f = open("./0713/myfile.txt", 'r')
# f_txt = f.read() # 파일의 내용을 읽어 str의 형태로 저장한다.
# print(f_txt)
# # print(type(f_txt))
# f.close()
# -----------------------------------------
# 'w'는 다 좋은데, 기존에 있던 내용을 지우면서 write를 수행한다.
# 'a'는 기존에 있던 내용에 값을 추가(add)하기 때문에 이런 걱정이 없다.
# f = open("./0713/myfile.txt", 'a')
# for i in range(11, 20):
#     d = '%d lines\n'%i # \n 없으면 줄바꿈을 안함
#     f.write(d)

# f.close()
# ----------------------------------------
# with문으로 파일에 자동으로 close() 적용해주기
# with open('./0713/myfile.txt', 'r') as f:
#     print(f.read()) # with 블록을 벗어나는 순간에 자동으로 close() 적용

# ----------------------------------------
# Quiz - 파일 읽기 문제
# dream1.txt 파일을 읽어 아래와 같이 파일의 내용 전체를 문자열로 출력하시오.
# fd = open('dream1.txt', 'r')
# print(fd.read())
# fd.close()

# 텍스트의 통계 정보를 읽어와야 할 때, split() 함수와 len() 함수를 사용한다.
with open('dream1.txt', 'r') as f:
    c = f.read()
    word_list = c.split(' ')
    line_list = c.split('\n')

print('total length:', len(c))
print('total words:', len(word_list))
print('total line:', len(line_list))



# -----------------------------------------
# 연습문제
# # 1. 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수를 작성해보자.
# def is_odd(number):
#     if number % 2 == 1:
#         return True
#     else:
#         return False

# print(is_odd(2456), is_odd(9783121))

# # 2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해보자. 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.
# def avg_numbers(*args): # 입력으로 들어오는 수에 개수에 상관없는 함수를 만들기 위해, '*'을 붙여준다.
#     result = 0

#     for i in args:
#         result += i

#     return result / len(args)

# print(avg_numbers(1,2), avg_numbers(1,2,3,5,4))

# # 3. 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다. 오류를 수정하여라.
# # input1 = input('1st num: ')
# # input2 = input('2nd num: ')

# # # tot = input1 + input2
# # tot = int(input1) + int(input2)
# # # print('sum is %s'%tot)
# # print('sum is %d'%tot) # %s는 str를 의미한다. 계산을 위해서는 integer로 형 변환이 이루어져야 한다.


# # 4. 다음 중 출력 결과가 다른 것 한 개를 골라보자.
# print('you' 'need' 'python')
# print('you'+'need'+'python')
# print('you','need','python')
# print(''.join(['you', 'need', 'python'])) # join은 왼쪽의 문자열을 자신의 배열의 값 사이에 넣어 연결시키겠다는 의미

# # 5. 다음은 'test.txt'라는 파일에 'Life is too short' 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# '''
# f1 = open('test.txt', 'w')
# f1.write('Life is too short')

# f2 = open('test.txt', 'r')
# print(f2.read())
# '''
# # 이 프로그램은 우리가 예상한 문자열을 출력하지 않는다. 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해보자.
# f1 = open('test.txt', 'w')
# f1.write('Life is too short')
# f1.close() # close로 f1을 닫아주어야 한다.

# f2 = open('test.txt', 'r')
# print(f2.read())
# f2.close()

# 6. 사용자의 입력을 파일에 저장하는 프로그램을 작성해보자. 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.
# user_input = input('저장할 내용을 입력하세요:')
# f = open('test.txt', 'a')
# f.write(user_input)
# f.write('\n')
# f.close()

# 7. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 'java'라는 문자열을 'python'으로 바꿔 저장해보자.
# '''
# Life is too short
# you need java
# '''
# f = open('test1.txt','r')
# body = f.read()
# f.close()

# body = body.replace('java', 'python')

# f = open('test1.txt', 'w')
# f.write(body)
# f.close()








