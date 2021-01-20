## Function 함수

#### 사용 이유

- 코드의 재사용
- 가독성이 높음
- 유지보수: 기능별 분화

#### 함수 선언 및 호출

``` python
# 함수 선언
def function(parameter):
    #<code>
    return value
	# value는 있어도 되고, 없으면 None 반환
    
# 함수 호출
b=function(argument)
```

- Ex) 정렬 함수 sort(), sorted()

  ``` python
  a=[1,3,7,4]
  b=a.sort()
  > a= [1,3,4,7]
  > b= None
  ```

  ``` python
  a=[1,3,7,4]
  b=sorted(a)
  > a= [1,3,7,4]
  > b= [1,3,4,7]
  ```

  - sort(): 원본을 정렬. 반환값이 없음(None). 
  - sorted(): 원본을 건드리지 않고, 정렬된 값을 반환

#### Argument, Parameter

__Argument(전달인자)__: 함수의 입력값. 함수 호출 시 사용

- 위치 인자 Positional Arguments

  ``` python
  #func: a**2+b
  c= func(1,2) # c=3
  d= func(2,1) # d=5
  ```

  - 위치에 맞는 인자가 순서대로 전달됨

- 키워드 인자 Keyword Arguments

  ``` python
  #func: a**2+b
  c=func(a=1,b=2) #c=3
  d=func(a=2,b=1) #d=3
  ```

  - 순서에 상관없이 매개변수 이름에 일치하는 위치로 전달됨

- 주의할점

  -  키워드 인자 뒤에 위치 인자가 들어올수 없음

  ``` python
  c=func(a=1,2) #불가능
  ```

__Parameter(매개변수)__: 함수의 입력 변수 명. 함수 정의 시 사용

- 기본값 Default Parameter

  - 전달 인자값(argument)이 없는 경우 에러발생. 

  ``` python
  def cal(a,b):
      return a**2+b
  
  c=cal() # no arguments, error
  ```

  - 기본 인자값(parameter)을 설정하면 그 값으로 사용. 인자 값이 있으면 해당값 사용

  ``` python
  def cal(a=1,b=2):
      return a**2+b
  c=cal() # c=3
  ```

  - 주의할점

    ``` python
    def cal(a=1,b): # error
        return a**2+b
    ```

    - 기본 인자값 이후에 기본 값이 없는 인자를 넣을수 없음. 
    - 전달인자를 어느 위치에 넣어야 할 지 판단하기 어려움

- 가변 인자 리스트 (위치 인자 패킹)

  ``` python
  def func (a,b, *args)
  ```

  - 개수가 정해지지 않은 임의의 위치 인자를 받을 때 사용함.

    ``` python
    #Example
    print('a','b','c','d','e')
    > a b c d e
    ```

  - *args는 tuple로 처리함. 

    - Pointer(포인터)가 아님. 파이썬엔 포인터 없음

  - Parameter의 마지막에 사용

- 가변 키워드 리스트 (키워드 인자 패킹)

  ``` python
  def func (**kwargs)
  ```

  - 개수가 정해지지 않은 임의의 키워드 인자를 받을 때 사용함.
  - **kwargs는 dictionary로 처리함.

- parameter 사용 순서 _사용할때 다시 찾아보자_

  ``` python
  def func (pos1,pos2, def1=val1,def2=val2, *arg, kw_only_arg,**kwarg):
  ```

  ![img](https://media.vlpt.us/images/ifyouseeksoomi/post/81272e0d-54fc-4101-a76f-23744dca1045/image.png)

  1. 일반 positional 인자
  2. 디폴트 인자 (이미 값을 지정한 인자)
  3. 가변 인자 (*args)
  4. Keyword-Only 인자
     - 다음 두개가 번갈아 가며 나옴
       - 디폴트가 아닌 Keyword-Only 인자
       - 디폴트 Keyword-Only 인자
  5. 가변 키워드 인자 (**kwargs)

#### Scope 스코프

1. Global Scope, Local Scope
   - Global Scope: 어디에서든 참조 할수 있는 공간
   - Local Scope: 함수가 생성한 공간. 함수 내부에서만 참조할수 있는 공간
2. Global Variable, Local Variable
   - Global Variable: Global scope에 정의된 변수
   - Local Variable: Local scope에 정의된 변수. Global scope에서 사용불가
3. 이름 검색 규칙 Resoultion 
   - LEGB Rule. LEGB 순으로 이름을 찾음. 중복되는 경우에 앞부분 부터 사용
     - Local scope: 정의된 함수
     - Enclosed scope: 상위 함수
     - Glogbal scope: 함수 밖의 변수 혹은 import된 모듈
     - Buiilt-in scope: 파이썬안에 내장되어 있는 함수 또는 속성 (내장함수)
4. 변수의 수명 주기 
   - local scope
     -  함수가 호출될 때 생성
     - 함수가 종료될 때까지 삭제
     - 함수 내에서 처리되지 않는 예외를 일으킬 때 삭제
   - global scope
     - 모듈이 호출된 시점 이후, 이름 선언된 이후 생성
     - 인터프리터가 끝날때 삭제
   - Built-in scope
     - 파이썬이 실행된 이후부터 영원히 유지



## Recursive Function 재귀 함수 

- 함수 내부에서 자기 자신을 호출 하는 함수

관련 유머

> 어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
>
> "재귀함수가 뭔가요?"
>
> "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어. 마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지. 그의 답은 대부분 옳았다고 하네. 
>
> 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.
>
> >  "재귀함수가 뭔가요?"
> >
> > "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을...

- 코드가 직관적이고 이해하기 쉬워 알고리즘 구현시 유용하게 활용됨.

  - 점화식을 코드로 구현하면 재귀 함수가 됨.
  - 점화식: 수열에서 이웃하는 두개의 항 사이에 성립하는 관계를 나타낸 관계식
  - _f_(0)=0, _f_(1)=1, _f_(_n+2_)=_f_(_n+1_)+_f_(_n_)

  ``` python 
  #Fibonacci
  def fibo(n):
      if n==0 or n==1:
          result=n
      else:
          result= fibo(n-1)+ fibo(n-2)
      return result
  ```

- 재귀 함수가 끝나는 시점(base case)이 필요함.

  - 범위가 줄어드는 점화식이나 일정 조건일때 빠져 나가야됨

- 많이 쌓이면 시간이 오래 걸리고 메모리가 계속 쓰이므로 사용시 유의해야 함. 
  - 파이썬에는 최대 재귀 깊이가 설정이 되어있음. (최대 1000번)
  - 반복문으로 대체 가능. 동적계획법

## Error 에러, Exception 예외처리

#### Error

1. `SyntaxError`
   - `^`(parser)가 문제가 발생한 위치를 알려주지만 완전한 것은 아님.

#### Excetption

- `ZeroDivisionError  `: 0으로 나눈 경우
- `NameError`: 정의되지 않은 변수 호출
- `TypeError`: 
  - 자료형에 대한 타입 자체가 잘못 되었을 경우
  - 필수 argument 누락, argument 개수 초과
- `ValueError`
  - 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
  - 존재하지 않는 값을 찾고자 할 경우
- `indexError`:존재하지 않는 index로 조회할 경우
- `KeyError`:딕셔너리에서 Key가 없는 경우 
- `ModuleNotFoundError`: 모듈을 찾을 수 없는 경우
- `ImportError`: 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 
  - 존재하지 않는 클래스/함수 호출
- `KeyboardInterrupt`: 터미널 상 'ctrl+c'를 통해 종료하였을 때 발생

---

여기부터는 조금 더 보완할 것

####  Exception Handling

``` python
try:
    pass
except (Exception1) as err1:
    pass
except (Exception2) as err2:
    pass
else:
    pass
finally:
    pass
```

- try: 
- except:
- as:
- else:
- finaly:



#### Exception Raising

- raise: 예외를 강제로 발생

  ``` python
  raise <ErrorName>('message')
  ```

- assert: