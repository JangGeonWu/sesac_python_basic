# for문
# for i in range(0, 303, 3): # 시작, 끝, 증감 값
#     print(i)


# for i in [0, 303, 3]: # list에서의 for문
#     print(i)    


# for i in range(2, -2, -1):
#     print(i)

# for j in range(1,6,1):
#     print(j, end=' ')

# tot = 0
# for i in range(1, 11):
#     tot += i

# print("1부터 10까지의 합계:", tot)

# for i in range(501, 1001, 2):
#     tot += i

# print("500과 1000사이에 있는 홀수의 합계:", tot)

# for i in range (0, 100, 7):
#     tot += i

# print("0 ~ 100 사이의 7의 배수의 합계:", tot)
# -----------------------------------------------
# num = int(input('값을 입력하세요: '))
# it = int(input('증감값을 입력하세요: '))

# for i in range(it, num+1, it):
#     tot = tot + i

# print(f"1부터 {num}사이에 있는 {it}의 배수의 합계: {tot}")

# -----------------------------------------------
# sta = int(input('시작 값을 입력하세요: '))
# endnum = int(input('끝 값을 입력하세요: '))
# it = int(input('증감값을 입력하세요: '))

# for i in range(sta, endnum+1, it):
#     tot += i

# print(f"{sta}에서 {endnum}까지 {it}씩 증가시킨 값의 합계: {tot}")
# # -----------------------------------------------
# dan = int(input("단을 입력하세요: "))

# for i in range(1, 10):
#     print(f"{dan} X {i} = {dan * i}")

# print("\n\n")

# for i in range(9, 0, -1):
#     print(f"{dan} X {i} = {dan * i}")
# -------------------------------------------------
# 중첩 for문
# for i in range(0, 3):
#     for j in range(0, 2):
#         print(f"i = {i}, j = {j}")

# for i in range(2, 10, 1):
#     print(f"{i}단")
#     for j in range(1, 10):
#         print(f"{i} X {j} = {i*j}")
#     print("")

# -------------------------------------------------
# for문의 응용
# a = [(1,2), (3,4), (5,6)]

# for (first, last) in a:
#     print(f"{first} + {last} = {first + last}")
# -------------------------------------------------

marks = [90,25,67,45,80]

# num = 0
# for mark in marks:
#     num += 1
#     if mark >= 60:
#         print(f"{num}번 학생은 합격입니다.")
#     else:
#         print(f"{num}번 학생은 불합격입니다.")

# for i, v in enumerate(marks):
#     if v >= 60:
#         print(f"{i + 1}번 학생은 합격입니다.")
#     else:
#         print(f"{i + 1}번 학생은 불합격입니다.")

# for문과 continue
# for i, v in enumerate(marks):
#     if v < 60: continue

#     print(f"{i + 1}번 학생은 합격입니다.")

# for num in range(len(marks)):
#     if marks[num] < 60:
#         continue
#     print(f"{num + 1}번 학생은 합격입니다.")

# -------------------------------------------------
# sum = 0
# for i in range(1,11):
#     sum += i

# print(sum)

# -------------------------------------------------

# Quiz - 1부터 200까지의 합계를 구하세요(단, 3의 배수는 제외하고 더하세요)
sum = 0
for i in range(1, 201):
    if i % 3 != 0:
        sum += i

print(sum)

# -------------------------------------------------

# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i*j, end='\t')
#     print('')

# -------------------------------------------------

# Quiz 2
# 1 ~ 100까지의 합계에서 최초 1000을 넘게하는 숫자를 구하세요.
sum = 0
for i in range(1, 101):
    sum += i
    if sum >= 1000:
        print(f"최초로 1000을 넘게하는 숫자: {i} / 1 ~ {i}까지의 합계 : {sum}")
        break

# -------------------------------------------------
# '리스트' 내포(list comprehension)
a  = [1,2,3,4]

result = []

for num in a:
    result.append(num*3)

print(result)

result2 = [num * 3 for num in a] # 루프(for문) 부여
print(result2)

result3 = [num * 3 for num in a if num % 2 == 0] # 조건(if문) 부여
print(result3)

# 응용
result4 = [x*y for x in range(2, 10)
                for y in range (1, 10)] # 각각의 변수에 맞추어 for - if문 적용

print(result4)   


