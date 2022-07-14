
# a = 5.00e10
# b = 0.20e-10
# print(a)
# print(b)
# print('a*b=', a*b) # python의 숫자형 처리 방식에의 해 '1'이 아닌 '0.9999....'가 뜬다.

# print(0o37) # 8진수, (8*3) + 7 = 31
# # ascii code
# print(chr(0x4C))

# print(3+4)
# print(3**4)
# print(11 % 3) # '% = 나머지'
# print(11 % 4)
# print(11 / 4)
# print(11 // 4)


# 문자열
# print("a")

print("Python's favorite food is cherry")
print('"He is good" she says')
print('P\'s f')
print("\"Hey!\" she said")

# # 여러 줄의 문자열
print("first line \nsecond line")
print('''
first line
second line''')
print("newline: \\n \n,tabkey: \\t \t,backspace: 123\\b456 -> 123\b456")
# '\\'은 단순히 '\'를 화면에 출력하라는 의미이다.
print("concatenation(문자열 연결)" + "is +")
# 띄어쓰기 없이 문자열을 연결한다.
print("a","b") # print("a", end=" ")와 print("b")
print("a", end=" ")
print("b")
print("문자열 곱하기(*) 뒤에는 무조건 정수! " * 3)
print("python"*100)

# 인덱싱 Indexing


a = "Indexing is very important"
#----01234567890123456789012345
#"-"-65432109876543210987654321
print(a[0])
print(a[12])
print(a[-1])
print(a[-5])

# 슬라이싱
print(a[0:5]) # = a[0] + a[1] + a[2] + a[3] + a[4]로, a[5]는 해당 안된다
print(a[:5])

print(a[5:10])

print(a[17:])
print(a[17:10]) # 슬라이싱 할때 이렇게 대소관계 안맞추면 출력이 안된다.

information = "20010305Rainy"
year = information[0:4]
month = information[4:6]
day = information[6:8]
weather = information[8:]

print(year)
print(month)
print(day)
print(weather)

# yy-mm-dd 형태로 출력해보자
print(information[2:4] + '-' + month + '-' + day)

# --------------------------------------------------------------------------
# Quiz 1
# 1
print("이름\t나이\t지역\n오라클\t10\t영등포구\n파이썬\t3\t영등포구")
# 2
print("동해물과 백두산이 마르고 닳도록\n하느님이 보우하사 우리나라 만세")
# 3
Q3 = "안녕하세요"
print(Q3* 6)
# 4
print(Q3[0] + '\n' + Q3[1] + '\n' + Q3[2] + '\n' + Q3[3] + '\n' + Q3[4])
# 5
print(Q3[-1]+ '\n' + Q3[-2] + '\n' + Q3[-3] + '\n' + Q3[-4] + '\n' + Q3[-5])

# --------------------------------------------------------------------------
# Quiz 2
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[-7:]

print(yyyymmdd)
print(num)
print("gender:" , pin[-7])
print("gender:" , "man" if pin[-7] == '1' else "woman")
# --------------------------------------------------------------------------

# 문자열 포맷팅(string formating)
print("I ate %d apples."%3)

x = "I ate %d apples." % 3 # 이거 자체를 변수에 대입할 수 있다.
print(x)
y = "I ate %s apples." %'five'
print(y)

asdf = 7
z = "I ate %d numbers" % asdf
print(z)

# --------------------------------------------------------------------------
# # 소수점 표현
print("%0.4f"%3.1415914) # 소수점 넷째 자리까지 표시
print("%10.4f"%3.1415914) 
# '____3.1416' 총 열 자리를 할당해 소수점 넷째 자리까지 표시, 빈 공간은 ' '로 표현한다.

print("%10syo" % "hi") # 10s는 10개의 문자를 의미
# '________hi'yo
print("%-10syo"% 'hi') # -10s로 포맷팅 되는 문자를 '어디에 배치'할 지 정한다.
# 'hi________'yo

# --------------------------------------------------------------------------
# 문자열 포맷팅 2
print("I ate {0} apples.".format("five"))

sx = 6
print("I ate {0} {1}".format(sx, "bananas"))

# --------------------------------------------------------------------------
# Quiz 2
# 1
age = input("당신의 나이는 몇 살이세요?")
print("제 나이는 {0}입니다.".format(age))

# 2
name = input("당신의 이름은?")
print("제 이름은 {0}입니다.".format(name))

# 3
print("제 나이는 {0}이고, 이름은 {1}입니다.".format(age, name))

# --------------------------------------------------------------------------
