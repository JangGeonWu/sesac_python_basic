 # 자판기 역할을 수행하는 파이썬 파일
coffee = 10
while True:
    money = 0
    try:
        money = int(input('돈을 넣어 주세요: '))
    except ValueError:
        print("값을 다시 입력해주시기 바랍니다.")
        continue


    if money == 300:
        print('커피를 줍니다.')
        coffee -= 1
    elif money > 300:
        print(f'거스름돈 {money - 300}을 주고 커피를 줍니다.')
        coffee -= 1
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.')
    
    print(f"남은 커피의 양은 {coffee}개입니다.")

    if coffee == 0:
        print("커피가 떨어졌습니다. 판매를 중지합니다.")
        break