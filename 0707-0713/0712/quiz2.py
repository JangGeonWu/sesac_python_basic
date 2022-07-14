'''
Q1. x=[3,6,9,20,-7,5]의 값의 모든 요소에 10을 곱하여 저장한 뒤 출력하세요.
y = {'math':70, 'science':80, 'english':20}의 값의 모든 요소에 10을 더하여 저장한 뒤 출력하세요.
'''
# x=[3,6,9,20,-7,5]
# x = [x[i] * 10 for i in range(len(x))]
# print(x)

# y = {'math':70, 'science':80, 'english':20}
# # y1 = list(y.items())

# # for i in range(len(y1)):
# #     y[y1[i][0]] = y1[i][1] + 10

# for i in y:
#     y[i] += 10 # i에는 key값이 나온다.

# print(y)

'''
Q2. [3,6,9,20,-7,5] 리스트를 sort와 같은 함수를 사용하지 말고
for문을 활용하여 오름차순으로 정렬하시오. '''
# li = [3,6,9,20,-7,5]

# for i in range(len(li)-1, 0, -1):
#     for j in range(0, i):
#         if li[j] > li[j+1]:
#             li[j], li[j+1] = li[j+1], li[j]

# print(li)            
    
'''
Q3. 1 ~ 100까지 숫자 숭, 3과 5의 공배수일 경우 '3과 5의 공배수',
나머지 숫자 중 3의 배수일 경우 '3의 배수', 나머지 숫자중 5의 배수일
경우 '5의 배수', 모두 해당되지 않을 경우 그냥 숫자를 출력하세요.
'''
for i in range(1, 101):
    if i % 15 == 0:
        print('3과 5의 공배수')
    elif i % 3 == 0:
        print('3의 배수')
    elif i % 5 == 0:
        print('5의 배수')
    else:
        print(i)

