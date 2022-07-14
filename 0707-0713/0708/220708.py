# aa = [0,0,0,0]

# aa[0]=int(input("1: "))
# aa[1]=int(input("2: "))
# aa[2]=int(input("3: "))
# aa[3]=int(input("4: "))

# print('total =', sum(aa))

aa = []

# aa.append(0)
# aa.append(0)
# aa.append(0)
# aa.append(0)

# print(aa)


# for i in range(0, 100):
#     aa.append(i)

# print(len(aa))
# print(aa)

for i in range(0,4):
    aa.append(0)

hap = 0

for i in range(0, 4):
    aa[i] = int(input(str(i+1) + "번째 숫자 : "))
    hap += aa[i]

print(f"합계 = {hap}")
