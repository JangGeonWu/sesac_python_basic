# Quiz-0707
# 1
sesac1=['red', 'blue', 'green']
print("1)", sesac1[0])
print("2)", sesac1[-1])
print("3)", len(sesac1))

#2
sesac = "python1"
print(sesac)
print(sesac[3:])
print(sesac[:3])
print(sesac[:4])
print(sesac[:-1])

#3
sesac2 = ['orange', 'black', 'white']

print(sesac1 + sesac2)
print(sesac1 * 2)
print(sesac1 + sesac2[:-1])

#4
mySesac= [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

print(mySesac[0][1])
print(mySesac[1][-1])
print(mySesac[2])

#5
sesac5 =  [ '설현' , '초아' , '지민', '유나' , '유경', '혜정' , '민아', '찬미' ]
print(sesac5[2])
print(sesac5[-2])
print([sesac5[0]])
print(sesac5[-2:])
print(sesac5[1:3])
print([sesac5[1], sesac5[4], sesac5[-1]])

#6
## 동전 교환 시스템 ##
money = int(input("교환할 돈은 얼마? "))

c50000 = money // 50000
money %= 50000

c10000 = money // 10000
money %= 10000

c5000 = money // 5000
money %= 5000

c1000 = money // 1000
money %= 1000

## 결과 print ##
print(f"교환 결과:\n50000원 {c50000}장\n10000원 {c10000}장\n5000원 {c5000}장\n1000원 {c1000}장")

if money != 0: print(f"바꾸지 못한 돈 ==> {money}원")