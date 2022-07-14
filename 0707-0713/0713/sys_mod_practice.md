# 파이썬에서는 sys 모듈을 사용하여 매개변수를 직접 줄 수 있다.
- sys 모듈을 사용하려면, import sys 명령어를 사용해야 한다.

> 명령 프롬프트 명령어 [인수1 인수2 인수3 .....]

다음 예시의 결과값은 아래와 같다.
```python
import sys

args = sys.argv[1:] # 입력받은 인수를 리스트의 형태로 args에게 전송

for i in args:
    print(i)

print(type(args))
```

![png](../images/sys1.PNG)

___

다음 예시의 결과값은 아래와 같다.
```python
import sys

args = sys.argv[:] # 이렇게 argv[1:]이 아닌 argv[:]을 쓰면, args[0]은 'sys2.py'가 된다. 주의!

for i in args:
    print(i.upper(), end=' ')
```

![png](../images/sys2.PNG)

___

# 생성한 모듈 사용하기
```python
# mod1.py
def add(a, b):
    return a+b

def sub(a,b):
    return a-b
```

- import 명령어를 통해 모듈을 불러와서 사용한다.

    ![png](../images/mod1.PNG)

- mod1.add처럼 쓰지 않고, add처럼 모듈 이름(mod1) 없이 함수 이름만 쓰고 싶은 경우에는 다음과 같이 사용하면 된다.

    > from mod_name import mod_function

    ![png](../images/mod2.PNG)

- 모듈의 여러 함수를 사용하고 싶을 때는 아래의 두 방법을 이용하면 된다.

    > from mod_name import mod_func1, mod_func2 ...

    혹은

    > from mod_name import *   

    ![png](../images/mod3.PNG)

- 다음 조건으로  파일을 직접 실행할 때만 수행하도록 할 수 있다.

    ```python
    def add(a, b):
    return a+b

    def sub(a,b):
        return a-b

    if __name__ == '__main__':
        print(add(1, 4))
        print(sub(4, 2))
        # __name__ == '__main__'은 직접 파일을 실행할 때(cmd> PYTHON mod2.py)만 실행되도록 함
    ```

    ![png](../images/mod4.PNG)

- 아래는 클래스나 변수 등을 포함한 모듈의 사용 예시이다.

    ```python
    # 클래스나 변수 등을 포함한 모듈
    PI = 3.141592

    class circle_area:
        def solv(self, r):
            return PI * (r ** 2)

    def add(a, b):
        return a+b
    ```

    ![png](../images/mod5.PNG)


- 다른 파일에서 모듈 불러오기를 수행하여보자.
    ```python
    # modtest.py
    import mod2
    result = mod2.add(3,4)
    print(result)
    ```
    - 실행하면 7이 출력된다. 이때 modtest.py와 mod2.py는 동일한 디렉터리에 위치해야 한다  :)

- sys.path.append
    - 다음 명령어로 (우리가 import하는) 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여준다.
    ![png](../images/sys3.PNG)

    - 다음 명령어로 sys.path에 원하는 경로를 입력하면

    > sys.path.append('C:/Users/User/Desktop/mydirectory')

    - 해당 경로(여기서는 mydirectory라는 디렉토리)에 있는 모듈을 '아무 곳에서나' 불러 사용할 수 있다.