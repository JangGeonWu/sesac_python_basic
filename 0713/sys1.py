import sys

args = sys.argv[1:] # 입력받은 인수를 리스트의 형태로 args에게 전송

for i in args:
    print(i)

print(type(args))