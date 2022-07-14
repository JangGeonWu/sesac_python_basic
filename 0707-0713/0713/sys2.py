import sys

args = sys.argv[:] # 이렇게 argv[1:]이 아닌 argv[:]을 쓰면, args[0]은 'sys2.py'가 된다. 주의!

for i in args:
    print(i.upper(), end=' ')