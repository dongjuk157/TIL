# Python

### 목차

[데이터](#데이터)

[Control Flow 제어문](#Control-Flow-제어문 )

[Function 함수](#Function-함수)

[Recursive Function 재귀 함수](#Recursive-Function-재귀-함수 )

[Error 에러](#Error-에러)

[데이터 구조](#데이터-구조)

[모듈, 패키지](#모듈,-패키지)

[Object Oriented Programming](#Object-Oriented-Programming)

---

환경: python 3.8 

- Python 공식 Tutorial https://docs.python.org/3.8/tutorial/index.html

Jupyter Notebook

- 설치: 

  ``` shell
  pip install notebook
  ```

- 실행: 

  ``` shell
  jupyter notebook
  ```

- Jupyter Notebook(REPL; Read Eval Print Loop)

  - 실행환경을 셸 단위의 코드 실행가능 
  - 마크다운 문법 사용가능
  - 머신러닝 등에 사용됨

PEP-8 https://www.python.org/dev/peps/pep-0008/

- Python 을 사용시 스타일에 맞게 작성하는 것이 좋음.



## 데이터

### 기초문법

1. 주석

   - 한줄 

   ``` python
   # 한줄주석
   ```

   - 여러줄

   ``` python
   '''
   여러줄
   주석
   '''
   ```

2. 코드라인

   - 한 줄에 한 문장
   - `;` 은 잘 쓰이진 않으나 한 줄 코드에서 문장 구분용도로 사용.
   - print 함수에서 여러줄을 작성하려면 `\`역슬래시도 가능함. (PEP-8에는 ''' 권장)

   ``` python
   print(''' hello,
   world
   !''')
   ```

- 문장, 표현식
  - 문장: 실행 가능한 최소한의 코드.
    - 문장은 표현식이 아닌것도 포함함.
    - radius =10 : 할당문은 표현식이 아님
  - 표현식: 하나의 값으로 환원될 수 있는 문장 (식별자, 값, 연산자로 구성)
    - print() 함수는 return하는 값은 없으나 None을 반환하므로 표현식임



### 변수

- 계산 결과를 상자에 넣어두고, 상자에 이름을 붙이는 느낌

- `a = 10` 

- `type()`: 변수의 데이터 타입 확인 가능

- `id()`: 값의 메모리 주소를 확인 가능

- 식별자: 이름. 변수, 함수, 모듈, 클래스 등등의 이름

  - 알파벳, _(underbar), 숫자를 사용할 수 있지만, 첫 글자에 숫자는 불가능
  - 대소문자 구분
  - 키워드는 사용할 수 없음.`import keyword; print(keyword.kwlist)`로 확인 가능
  - 일반적으로 사용되는 함수의 이름도 사용하지 않는 것이 좋음. 같은 이름의 함수는 기능을 수행하지 못함

  ```python
  print = 0
  print("hello,python")
  ```



### 데이터 타입

1. 숫자(int, float, complex)

   **Integer**  `int`

   - 정수의 범위가 한정되지 않음. Overflow 없음.

     -> 임의 정밀도 산술: 남아있는 만큼의 가용 메모리 사용 가능

      C/ C++는 64 bits의 정밀도 사용

   - 숫자 앞에 적어서 다음을 표현할수 있음. 2진수 `0b`, 8진수 `0o`, 16진수 `0x` 

   **Floating point number**  `float`

   - `pi=314e-2` 와 같은 표현 가능
   - 실수 연산시 오류가 발생할수 있음(floating point rounding error)

   ``` python
   3.5-3.12
   print(3.50-3.12)
   >0.3799999999999999
   ```

   - `round()`, `math.isclose(a,b)`, `sys.float_info.epsilon` 등을 사용해서 처리

   **Complex number**

   - `a=3-4j`
   - `.imag`, `.real` 을 사용하여 각각 접근할 수 있음
   - 문자열에서 복소수로 변환할 때 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 됨

2. 문자

   - 똑같이 보이는 것도 타입이 다를수있음. `type()`으로 형 확인 필수
   - `input()`으로 받으면 무조건 ‘str’ 타입으로 받음
   - String interpolation: 문자열안에 변수를 넣는 방법. 세가지 방법 다 알아야됨

   ```python
   #%-formatting
   print('Hello, %s' % name)
   
   #str.format()
   print('Hello, {}'.format(name))
   
   #f-strings : 파이썬 3.6 이후 버전에서 지원
   print(f'Hello, {name}')
   ```

3. 참/거짓, None

   - Bool 타입 `True` `False`
   - 다음은 False로 변환 `0, 0.0, (), [], {}, '', None`
   - `None`: 값이 없음

4. 형변환

   - 암시적 형변환: 파이썬이 자동으로 형 변환.  Bool, Numbers(int,float,complex)에서 더 큰 그룹으로 형변환

   ```python
   True+5 	# 6 <class 'int'>
   3 + 4.5 # 7.5 <class 'float'>
   ```

   - 명시적 형변환: 사용자가 직접 형 변환

   ``` python
   a= 5.5			# 5.5 <class 'float'>
   print(int(5.5)) # 5 <class 'int'>
   ```

   

### 연산자

1. 산술

| 연산자 | 내용                |
| ------ | ------------------- |
| +      | 덧셈                |
| -      | 뺄셈                |
| \*     | 곱셈                |
| /      | 나눗셈 (float 반환) |
| //     | 몫 (int 반환)       |
| %      | 나머지(modulo)      |
| \*\*   | 거듭제곱            |

2. 비교

|   연산자 |                   내용 |
| -------: | ---------------------: |
|      `<` |                   미만 |
|     `<=` |                   이하 |
|      `>` |                   초과 |
|     `>=` |                   이상 |
|     `==` |                   같음 |
|     `!=` |               같지않음 |
|     `is` |        객체 아이덴티티 |
| `is not` | 부정된 객체 아이덴티티 |

- bool 로 반환
- `is`, `is not`은 객체(object)

3. 논리

|  연산자 |                         내용 |
| ------: | ---------------------------: |
| a and b |     a와 b 모두 True시만 True |
|  a or b |  a 와 b 모두 False시만 False |
|   not a | True -> False, False -> True |

- 단축평가

  - 판단을 하지 않아도 되므로 속도 향상

  - 첫번째 값이 확실할때 두번째 값을 확인하지 않음.

  - `A and B`:

    `A==0`이면  `B`를 확인할 필요없이 바로 `False` -> `A`출력

    `A!=0`이면  `B`에 의해 결정되므로 `B`출력

  - `A or B`:

    `A==0`이면 `B`에 의해 결정되므로 `B`출력

    `A!=0`이면 `B`를 확인할 필요없이 `True` -> `A`출력

4. 복합

   |  연산자 |       내용 |
   | ------: | ---------: |
   |  a += b |  a = a + b |
   |  a -= b |  a = a - b |
   |  a *= b |  a = a * b |
   |  a /= b |  a = a / b |
   | a //= b | a = a // b |
   |  a %= b |  a = a % b |
   | a **= b | a = a ** b |

5. 기타

   - Concatenation: 숫자가 아닌 자료형은 `+`으로 합칠 수 있음
   - Containment: `in`를 사용하여 요소가 속해있는지 확인할 수 있음
   - Identity: `is` 동일한 Object인지 확인 가능
   - Indexing: `a[index]` 으로 값에 접근가능
   - Slicing: `a[:]`으로 슬라이싱 가능
   - 연산자 우선순위
     1. `()`을 통한 grouping
     2. Slicing
     3. Indexing
     4. 제곱연산자 `**`
     5. 단항연산자 `+`, `-` (음수/양수 부호)
     6. 산술연산자 `*`, `/`, `%`
     7. 산술연산자 `+`, `-`
     8. 비교연산자, `in`, `is`
     9. `not`
     10. `and`
     11. `or`



### Container

#### 시퀀스형 컨테이너

순서를 가질 수 있어서 특정 위치의 데이터를 가리킬 수 있다.

1. List

   - 다른 프로그래밍 언어에서는 Array(배열)라고 불림
   - `[]` `list()` 로 선언. `list[i]`로 접근.

2. Tuple

   - 직접 활용하는 것보다 간접적으로 활용하는 경우가 많음
   - 변경, 수정이 불가능함(불변, immutable). 
   - 읽기 속도가 리스트보다 빠름
   - `()` `tuple()`로 선언. 하나로만 구성하려면 comma를 넣어줌 `a=(1,)`

3. Range

   - 숫자의 시퀀스를 나타내기 위해 사용

   - 기본형 : `range(n)` 0부터 n-1까지 값을 가짐

     범위 지정 : `range(n, m)`n부터 m-1까지 값을 가짐

     범위 및 스텝 지정 : `range(n, m, s)` n부터 m-1까지 +s만큼 증가한다

   - list로 사용하려면 형변환 필수

4. String, Binary

5. 활용할수 있는 연산자 함수.

   |    operation |                    설명 |
   | -----------: | ----------------------: |
   |     x `in` s |        containment test |
   | x `not in` s |        containment test |
   |    s1 `+` s2 |           concatenation |
   |      s `*` n | n번만큼 반복하여 더하기 |
   |       `s[i]` |                indexing |
   |     `s[i:j]` |                 slicing |
   |   `s[i:j:k`] |       k간격으로 slicing |
   |       len(s) |                    길이 |
   |       min(s) |                  최솟값 |
   |       max(s) |                  최댓값 |
   |   s.count(x) |                x의 개수 |

#### 비 시퀀스형 컨테이너

1. Set
   - `{val1,val2,val3}` `set()`으로 선언가능. 빈 집합은 `{}`로 불가능
   - 순서가 없고, 중복도 없음
   - 합집합`|`, 차집합`-`, 교집합`&`
   - list의 중복된 값을 지울때 사용
2. Dictionary
   - `{Key: value}`  `dict()` 로 선언
   - Key는 변경할수 없고 중복된 값도 존재할 수 없음. 
   - `dic[Key]==Value #True` key로 Value를 찾을수 찾을수 있음
   - `Keys()`, `values()`,`items() 리스트 모양이지만 리스트는 아님
   - `items()` 튜플로 묶인 원소들로 만들어짐 `[(key1,value1),(key2,value2)]`

#### 형변환

![typecasting](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)

#### 참고

변경 가능한 데이터(mutable 데이터)의 복사. 참조형 변수

- Int, boolean 는 변수에 해당 값을 할당

  ``` python
  num1= 20
  num2= num1
  num2= 10
  >> num1 =20, num2 =10
  ```

- List, dict, set는 변수에 주소 값을 할당

  - 주소값을 지정하므로 값을 바꾸면 연결되어있는 모든 곳들도 변경되므로 유의해서 사용

  ``` python
  num1= [1,2,3,4]
  num2= num1
  num2[0]= 100
  >> num1 =[100,2,3,4], num2 =[100,2,3,4]
  ```

  - 해결방법: 새로 선언해서 해결. `b=list(a)`,`b=a[:]`,`deepcopy`



## Control Flow 제어문

Flow Chart 중요



### 1. 조건문(If Statement)

python에서는 들여쓰기(tab, 4spaces)를 맞춰줘야 함.

그렇지 않으면 `IndentationError`가 뜸

``` python
if <조건식>:
    <code1> #4 space or tab
elif <조건식>:
    <code2>
else:
    <code3>
```

- 조건표현식(삼항연산자)
  - `true_value if <조건식> else false_value`
  - 표현식이므로 하나의 값임.
  - 조건문을 사용하지 못하는 경우나 간결한 코드를 위해 사용



### 2. 반복문(Loop Statement)

1. while

   - 조건식이 참(True)인 경우에만 코드 실행

   ``` python
   while <조건식>:
       <code>
   ```

   - 코드 내 종료 조건 필요. 무한 루프 가능성

2. for

   - 시퀀스(string, tuple, list, range)나 다른 순회가능한 객체(iterable)의 요소들을 순회함.

   ``` python
   for num in nums: 	# nums = [10,20,30,40,50]
       print(num)  	
       # 10
       # 20
       # 30
       # 40 
       # 50
   ```

   - 다른 언어에서는 인덱스로 접근
   - enumerate
     - 인덱스(index)와 값(value)을 함께 활용 가능
     - 튜플로 반환 (index1,value1)
     - start 숫자 지정가능

   ``` python
   for i, num in enumerate(nums,start=1): 	# nums = [10,20,30,40,50]
       print(i,num)  	
       # 0 10
       # 1 20
       # 2 30
       # 3 40
       # 4 50
   ```

   ``` python
   print(enumerate(nums))
   #<enumerate object at (memory address)>
   print(list(enumerate(nums)))
   #[(0,10),(1,20),(2,30),(3,40),(4,50)]
   ```

3. 반복제어

   - break: 반복문 종료

     ``` python
     for num in range(5):
     	if num == 2:
             break
         print(i)
         # 0
         # 1
         # break. 반복문 종료
     ```

   - continue: continue 이후의 코드를 수행하지 않고, 다음 요소부터 다시 반복 진행

     ``` python
     for num in range(5):
     	if num == 2:
             continue
         print(i)
         # 0
         # 1
         # continue. 이후 코드는 무시하고 다음 요소 진행
         # 3
         # 4
     ```

   - for-else, while- else

     - 끝까지 반복문을 실행한 이후에 실행
       - `for`문에서 리스트가 소진 되었을 경우
       - `while`문에서 조건이 거짓이 돼서  종료된 경우
     - 반복문이 `break` 문으로 종료될 때는 실행되지 않음

     ```python
     # 리스트 안에 값이 있는지 찾는 코드
     menu = ['칼국수','돌솥비빔밥','주꾸미볶음']
     for mn in menu:
         if mn =='치킨':
             print('치킨 좋네')
             break
     else:
         print("치킨 먹자")
     #menu에 '치킨'이 없으므로 '치킨먹자' 출력
     ```

     - for-else를 사용하지 않고도 같은 코드를 만들수있음. (다른 언어에서 사용)

     ``` python
     menu = ['칼국수','돌솥비빔밥','주꾸미볶음']
     cnt=True
     for mn in menu:
         if mn =='치킨':
             print('치킨 좋네')
             cnt=False #break이 되었는지 확인
             break
     if cnt:
         print("치킨 먹자")
     #menu에 '치킨'이 없으므로 '치킨먹자' 출력
     ```

     

   - pass: 아무것도 하지 않음

     - 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 자리를 채우는 용도
     - 코드를 만들지 않았는데 이전까지 문제없는지 확인하고 싶은 경우에 사용했음.



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
     -  함수가 종료될 때까지 삭제
     -  함수 내에서 처리되지 않는 예외를 일으킬 때 삭제
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
> >  "잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을...

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



## Error 에러

#### Syntax Error 문법 에러

- `^`(parser)가 문제가 발생한 위치를 알려주지만 완전한 것은 아님.
- EOL: End of Line
- EOF: End of File



#### Excetption 예외

- 문법적으로는 문제 없고 실행시 발생하는 에러

- `ZeroDivisionError  `: 0으로 나눈 경우
- `NameError`: 정의되지 않은 변수 호출
- `TypeError`: 
  - 자료형에 대한 타입 자체가 잘못 되었을 경우
  - 필수 argument 누락
  - argument 개수 초과
- `ValueError`
  - 자료형에 대한 타입은 올바르나 값이 적절하지 않는 경우
  - 존재하지 않는 값을 찾고자 할 경우
- `indexError`:존재하지 않는 index로 조회할 경우
- `KeyError`:딕셔너리에서 Key가 없는 경우 
- `ModuleNotFoundError`: 모듈을 찾을 수 없는 경우
- `ImportError`: 모듈을 찾았으나 가져오는 과정에서 실패하는 경우 
  - 존재하지 않는 클래스/함수 호출
- `KeyboardInterrupt`: 터미널 상 'ctrl+c'를 통해 종료하였을 때 발생



####  Exception Handling 예외 처리

예외 처리를 하지 않으면 프로그램, 웹사이트, 서버 등이 정상적으로 동작하지 않음

``` python
try:
    <code 1>
except (Exception1, Exception2) as err1:
    <code 2>
    print(err1)
except (Exception3)
    <code 3>
except:
    <code 4>
else:
    <code 5>
finally:
    <code 6>
```

- `try`:  Exception이 발생할수 있는 코드 작성. 
- `except`
  - `try`에서 exception이 발생하면 실행하고 발생하지 않으면 넘어감
  - 각 exception 마다 지정하여 처리 가능. 
  - Exception을 묶어서 처리 가능
  - 지정하지 않은 모든 에러에 대해서 처리 가능
- `as`: 에러 메세지의 내용까지 알고 싶을때 사용
- `else`: Exception이 발생하지 않은 경우 실행
- `finaly`
  - 예외 발생과 상관 없이 항상 수행
  - 보통 사용한 리소스를 close 할때 많이 사용. 



#### Exception Raising

- raise: 예외를 강제로 발생

  ``` python
  raise <ErrorName>('message')
  ```

  - 사용자가 직접 설정하게 에러만 발생시킴.

- assert

  - 상태를 검증하는데 사용. 디버깅용도.
  - 무조건 AssertionError가 발생



## 데이터 구조

데이터에 편리하게 접근하고, 변경하기 위해서 데이터를 저장하거나 조작하는 방법

- 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조
  - 문자열(String)
  - 리스트(List)
- 알고리즘에 빈번히 활용되는 순서가 없는(unordered) 데이터 구조
  - 세트(Set)
  - 딕셔너리(Dictionary)

- 데이터 구조에 적용 가능한 Built-in Function



### 문자열(String)

변경불가능(**immutable**), 순서있음(ordered), 순회가능(iterable)

- `.find(x)`: x의 첫 번째 위치를 반환합니다. 없으면, -1을 반환

- .`index(x)`: x의 첫번째 위치를 반환합니다. 없으면, 오류가 발생.

- `.replace(old, new[, count])`:

  바꿀 대상 글자를 새로운 글자로 바꿔서 반환. count를 지정하면 해당 갯수만큼만 시행

- `.strip([chars]) .lstrip([chars]), .rstrip([chars])`
  특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거합니다(rstrip). 지정하지 않으면 공백을 제거.

- `.split()` :문자열을 특정한 단위로 나누어 리스트로 반환

- `'separator'.join(iterable):`

  반복가능한 컨테이너의 요소들을 구분자(separator)로 합쳐 문자열로 반환.

- `.capitalize()` : 앞글자를 대문자로 만들어 반환

- `.title()` : 특정 위치만 대문자로 만들어 반환

- `.upper()` : 모두 대문자로 만들어 반환

- `lower()` : 모두 소문자로 만들어 반환

- `swapcase()` : 대 <-> 소문자로 변경하여 반환

- 기타 문자열 관련 검증 메소드 : 참/거짓 반환

  `.isalpha()`, `.isdecimal()`, `.isdigit()`, `.isnumeric()`, `.isspace()`, `.isupper()`, `.istitle()`, `.islower()`



### 리스트(List)

변경가능(**mutable**), 순서있음(ordered), 순회가능(iterable)

- `.append(x)`: 값을 추가

- `.extend(iterable)`: iterable(list, range, tuple, string) 값

  - iterable의 요소가 더해지므로 string의 경우 나뉘어서 더해짐.

- `.insert(i, x)`: 정해진 위치 i에 값을 추가

- `.remove(x)`: 값이 x인 것을 삭제

- `.pop(i)`: -> set, dictionary

  정해진 위치 i에 있는 값을 삭제하며, 그 항목을 반환. i가 지정되지 않으면 마지막 값

- `.clear()`: 모든 항목을 삭제

- `.index(x)`: x 값을 찾아 해당 index 값을 반환. index 없는 경우 에러 발생

- `.count(x)`: 원하는 값의 개수를 확인

- `.sort()`: 정렬. 내장함수 sorted() 와는 다르게 원본 list를 변형시키고, None을 리턴.

- `.reverse()`:   반대로 뒤집음.

**리스트 복사**

- Shallow copy: Slicing, list()
- Deep copy: 
  - `import copy` `copy.deepcopy(list)`

**리스트 comprehension**

- `[expression for 변수 in iterable if 조건식]`
- 조건식이 참인 경우만 리스트의 요소로 들어감



### 데이터 구조에 적용가능한 Built-in Function

순회 가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

#### 람다(lambda)

`lambda <parameter> : <expression>`

한 줄 함수

ex)

```python
def hap(x, y):
	return x + y
hap(10, 20) # =>30

(lambda x,y: x + y)(10, 20) # => 30 같은식
```

#### map(function, iterable)

원소를 하나씩 꺼내서 함수를 적용시킨 후으로 `map_object`를 반환. 

- 주의. function은 이름만 작성

ex)

```python
list(map(lambda x: x ** 2, range(5)))    
# [0, 1, 4, 9, 16]
list(map(int,input().split())) # => 알고리즘에 자주쓰임
```

#### filter(function,iterable)

원소들을 함수에 적용시켜 결과가 참인 값들로 `filter object`를 반환

-  `False`로 형변환이 되지 않는 모든 것들은 `True`로 동작

```python
list(filter(lambda x: x % 2, range(10))) 
#[1, 3, 5, 7, 9]
```

#### zip(*iterables)

iterable 객체를 모아 튜플의 모음으로 구성된 `zip object` 를 반환

- 튜플의 길이는 가장 짧은 iterable 객체의 길이
- 두개를 사용하면 dictionary 만들기 좋음

#### reduce(function,iterable)

순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적하면서 함수에 적용

ex)

```python
from functools import reduce # import 필요
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])
#10
reduce(lambda x, y: y + x, 'abcde')
#'edcba'
```



### 세트 (set)

변경 가능(__mutable__), 순서 없음(__unordered__), 순회 가능(iterable)

- .add(elem): elem을 세트에 추가
- .update(*others):
  -  여러가지의 값을 추가합니다.
  -  인자로는 반드시 iterable 데이터 구조 전달
- .remove(elem): elem을 세트에서 삭제, 없으면 KeyError 발생
- .discard(elem): elem을 세트에서 삭제, 없어도 에러가 발생안함
- .pop(): (순서가 없어서) 임의의 원소를 제거해 반환.



### 딕셔너리(Dictionary)

변경 가능(__mutable__), 순서없음(__unordered__), 순회 가능(iterable)

- .get(key[, default]): 

  - key를 통해 value에 접근
  - 절대로 KeyError가 발생하지 않고 default는 None

- .pop(key[, default])

  - 딕셔너리에 있으면 key를 제거하고 value 반환. key 없으면 default를 반환

  - default가 없는 상태에서 딕셔너리에 없으면 KeyError 발생

- .update(): 값을 제공하는 key, value로 덮어씀

#### 딕셔너리 순회(반복문 활용)

```python
# key 활용
for key in dict:
    print(key)
    print(dict[key])

#keys() 활용
for key in dict.keys():
    print(key)
    print(dict[key])

#values() 활용    
for val in dict.values():
    print(val)

#items() 활용
for key, val in dict.items():
    print(key, val)
```

#### Dictionary comprehension

```python
{key: value for 변수 in iterable if 조건식}
```

List comprehension과 유사하게, 조건문에 참인 식으로 딕셔너리를 생성

ex)

```python
temperatures = {'서울': 9, '대전': 12, '구미': 13, '광주': 13, }
# 온도가 10도를 초과하는 지역만 뽑아주세요.
{key:value for key, value in temperatures.items() if value > 10}
# => {'대전': 12, '구미': 13, '광주': 13}
```



## 모듈, 패키지

> 파일 단위의 코드 재사용

- 모듈(Module):  특정 기능을 하는 코드를 담고 있는 파일(또는 스크립트)
- 패키지(Package): 점(`.`)으로 구분된 모듈 이름(`package.module`) 을 써서 모듈을 구조화하는 방법

| 용어                     | 정의                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 모듈                     | 특정 기능을 `.py` **파일 단위**로 작성한 것.                 |
| 패키지                   | 특정 기능과 관련된 여러 **모듈들의 집합**. 패키지 안에는 또다른 서브 패키지를 포함 할수도 있음. |
| 파이썬 표준 라이브러리   | 파이썬에 **기본적으로 설치된 모듈과 내장 함수**를 묶어서 파이썬 표준 라이브러리 (Python Standard Library, PSL) 라 불림. |
| 패키지 관리자(**`pip`**) | `PyPI` 에 저장된 외부 패키지들을 설치하도록 도와주는 패키지. |

#### 모듈(Module)

```python
import module
from module import var, function, Class
from module import * # 웬만하면 사용하지 말것
```

#### 패키지(Package)

```python
from package import module
from package.module import var, function, Class
from package.module import var as v # v로 사용할수 있음
```

- 패키지 생성하는 방법은 필요시 찾아볼 것



## Object Oriented Programming

객체 지향 프로그래밍

### 프로그래밍

1. 절차 지향 Procedural Programming

   프로시저 호출의 개념을 바탕으로 하고 있는 프로그래밍 패러다임

   - 프로시저: 루틴이나, 서브루틴 및 함수와 같은 뜻
   - 하나의 프로시저는 특정 작업을 수행하기 위한 프로그램의 일부
   - 프로그램의 아무 위치에서나 프로시저를 호출될 수 있는데, 다른 프로시저에서도 호출 가능하고 심지어는 자기 자신에서도 호출 가능하다.

2. 객체 지향

   객체 지향 프로그래밍은 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위(객체들의 모임)로 파악하고자 하는 것

   - 추상화
     - 너무 많은 정보를 알면 사용하기 어렵기 때문에 디자인을 단순하게 만듦
     - 각각의 부분에서 효율적으로 동작하게 함

   - 사용이유: 코드의 직관성, 활용의 용이성, 변경의 유연성

3. 함수형 프로그래밍?

   나중에 찾아볼것

   [함수형 프로그래밍 요약](https://velog.io/@kyusung/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%9A%94%EC%95%BD)

   

### 객체 Object

클래스에서 정의한 것을 토대로 메모리에 할당된 것. 

프로그램에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간

- Type 타입: 공통된 속성(attribute)과 조작법(method)을 가진 객체들의 분류
- Instance 인스턴스: 특정 타입(type)의 실제 데이터 예시
  -  파이썬에서 모든 것은 객체이고, 모든 객체는 특정 타입의 인스턴스이다.
- Attribute 속성: 객체의 상태/데이터
  - 클래스 내부의 데이터
- Method 메소드: 특정 객체에 적용할 수 있는 행위
  - 클래스 내부에 정의된 함수
  - dir(list): 리스트가 사용할 수 있는 속성과 메소드 출력



### 클래스

```python
class <ClassName>: #<ClassName>은 PascalCase로 정의
    <statement>
```

**활용**

``` python
class Person:		# 클래스 정의
    population = 0								# 클래스 변수
    # Instance Method(인스턴스 생성시 실행되는 메서드)
    def __init__(self, name, age, birthday):	# 생성자
        self.name = name						# 인스턴스 변수
        self.age = age
        self.birthday = birthday
        Person.population += 1

    def greeting(self):
        print(f"Hi, Nice to meet you. My name is {self.name}.")
        
    def __del__(self):							# 소멸자
        Person.population -= 1							
        
    @classmethod	# Class Method
    def PrintPopulation(cls):
        print(cls.population)
    
    @staticmethod	# Static Method
    def PersonInfomation():
        print("Type is Person")
        
person1 = Person('Kim', 25, 'yyyy-mm-dd')	# 인스턴스 생성
person1.PrintPopulation()   # => 1
person1.PersonInfomation()  # => Type is Person
person1.greeting()	# => "Hi, Nice to meet you. My name is Kim."
```

- 인스턴스 변수: 인스턴스의 속성(attribute)
  - 각 인스턴스들의 고유한 변수. 인스턴스 내에서 사용하는 변수. 
  - 메서드 정의에서 `self.변수명`로 정의
  - 인스턴스가 생성된 이후 `인스턴스.변수명`로 접근 및 할당
- 클래스 변수: 클래스의 속성(attribute)
  - 클래스의 속성. 클래스 내에서 사용하는 변수
  - 모든 인스턴스가 공유
  - 클래스 선언 내부에서 정의
  - `클래스.변수명`으로 접근 및 할당
- 인스턴스 메서드
  - 인스턴스가 사용할 메서드
  - 클래스 내부에 정의되는 메서드의 기본값은 인스턴스 메서드
  - 호출시, 첫번째 인자로 인스턴스 자기자신 `self`이 전달됨
    - `self`:인스턴스 자신(self)
  - 인스턴스가 할 행동은 모두 인스턴스 메서드로 한정 지어서 설계할 것
    - 클래스 메서드와 스태틱 메서드는 접근 가능하나 사용하지 않는것이 좋음
  - ex) 생성자, 소멸자
- 클래스 메서드
  - 클래스가 사용할 메서드
  - `@classmethod` 데코레이터를 사용하여 정의
  - 호출시, 첫 번째 인자로 클래스 `cls`가 전달됨
  - 클래스에서 인스턴스 메서드는 호출하지 말 것(접근은 가능함)
- 스태틱 메서드
  - 클래스가 사용할 메서드
  - `@staticmethod` 데코레이터를 사용하여 정의
  - 호출시, 어떠한 인자도 전달되지 않음. 
    - self(인스턴스 변수)나 cls(클래스 변수)가 필요하지 않은 동작
    - 클래스와 클래스 속성에 접근할 필요가 없다면 **스태틱 메서드**로 정의

- 이름공간 탐색 순서
  - 클래스를 정의하면, 클래스가 생성됨과 동시에 이름 공간(namespace)이 생성
  - 인스턴스를 만들게 되면, 인스턴스 객체가 생성되고 해당되는 이름 공간이 생성
    - HEAP, Garbage Collector 찾아볼것.
  - 인스턴스의 속성이 변경되면, 변경된 데이터를 인스턴스 객체 이름 공간에 저장
  - 인스턴스에서 특정한 속성에 접근하게 되면 인스턴스 => 클래스 순으로 탐색



### 상속

#### 상속

```python
class ChildClass(ParentClass):
    <code block>
```

- 부모 클래스의 모든 속성들을 자식 클래스에서 사용하는 것

  - 부모 클래스에서 변경하면 자식 클래스에도 자동으로 적용됨
  - 코드의 재사용성이 높아짐

- `super()`

  - 부모 클래스의 내용을 사용하면서 자식 클래스에 메서드를 추가로 구현할 때 사용

  ```python
  class ChildClass(ParentClass):
  	def __init__(self, parent_common_value, child_only_value):# 메소드 오버라이딩 발생
          super().__init__(parent_common_value) 		# 상속받은 값을 사용함
          self.child_only_value = child_only_value	# 추가 작업
  ```

  

#### 메서드 오버라이딩 Method Overriding

- 자식 클래스에서 부모 클래스의 메서드를 재정의하는 것
- 상속 받은 클래스에서 같은 이름의 메서드로 덮어쓰는 것
- 이름 공간을 탐색해나가는 과정에서 상속관계에 있으면 확장됨
  - `.mro()`: method Resolution Order 로 확인가능
  - 인스턴스 -> 자식 클래스 -> 부모 클래스 -> 전역



#### 다중 상속

- 두개 이상의 클래스를 상속받는 것
- 상속 순서: 자식-> 부모(상속받을 때 순서) -> 상위 클래스

