'''
Q1. 사용자로 점수 3개를 입력받아 모든 점수가 65점보다 클 경우 합격
아닐 경우 불합격을 출력하세요. 단, 0 ~ 100이 아닌 숫자가 입력된 경우
'잘못된 점수가 입력되었습니다'를 출력하세요
'''
# a = []
# a.append(int(input('첫번째 점수를 입력해주세요: ')))
# a.append(int(input('두번째 점수를 입력해주세요: ')))
# a.append(int(input('세번째 점수를 입력해주세요: ')))

# state = 1

# for i in a:
#     if i < 0 or i > 100:
#         state = -1
#         break
#     elif i < 65:
#         state = 0
        
# if state == 0:
#     print("불합격")
# elif state == 1:
#     print("합격")
# else:
#     print("잘못된 점수가 입력되었습니다.")
'''
Q2. 유저로부터 카테고리와 상품명을 입력받아 카테고리가 과일일때는 fruit 리스트에
카테고리가 채소일때는 vegetable 리스트에 상품을 '추가'하고 리스트의 모든 내용을 출력하시오.
단, 카테고리가 채소나 과일이 아닐 경우 '존재하지 않는 카테고리입니다'
이미 등록 되어있는 경우 '이미 등록된 과일입니다' 혹은 '이미 등록된 채소입니다'를 출력하시오.
'''
fruit = ['사과', '오렌지']
vegetable = ['당근', '호박']

categ = input('등록할 카테고리를 선택해주세요(과일, 채소):')
item = input(f'등록할 {categ}을 입력해주세요: ')

if categ == '과일':
    if item in fruit:
        print('이미 등록된 과일입니다.')
    else:
        fruit.append(item)
        print(fruit)
elif categ == '채소':
    if item in vegetable:
        print('이미 등록된 채소입니다.')
    else:
        vegetable.append(item)
        print(vegetable)
else:
    print('존재하지 않는 카테고리입니다.')


