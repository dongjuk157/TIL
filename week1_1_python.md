# Python

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

### 1. 기초문법

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
   - print 함수에서 여러줄을 작성하려면 `\`역슬래시도 가능하나 다음을 사용하는 것을 추천.

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



### 2. 변수

- 계산 결과를 상자에 넣어두고, 상자에 이름을 붙이는 느낌

- `a = 10` 

- `type()`: 변수의 데이터 타입 확인 가능

- `id()`: 값의 메모리 주소를 확인 가능

- 식별자: 이름. 변수, 함수, 모듈, 클래스 등등의 이름

  - 알파벳, _(underbar), 숫자를 사용할 수 있지만, 첫 글자에 숫자는 불가능
  - 대소문자 구분
  - 키워드는 사용할 수 없음.
  - 일반적으로 사용되는 함수의 이름도 사용하지 않는 것이 좋음. 같은 이름의 함수는 기능을 수행하지 못함

  ```python
  print = 0
  print("hello,python")
  ```



### 3. 데이터 타입

1. 숫자(int, float, complex)

   Integer  `int`

   - 정수의 범위가 한정되지 않음. Overflow 없음.

     -> 임의 정밀도 산술: 남아있는 만큼의 가용 메모리 사용 가능

      C/ C++는 64 bits의 정밀도 사용

   - 숫자 앞에 적어서 다음을 표현할수 있음. 2진수 `0b`, 8진수 `0o`, 16진수 `0x` 

   Floating point number  `float`

   - `pi=314e-2` 와 같은 표현 가능
   - 실수 연산시 오류가 발생할수 있음(floating point rounding error)

   ``` python
   3.5-3.12
   print(3.50-3.12)
   >0.3799999999999999
   ```

   - `round()`, `math.isclose(a,b)`, `sys.float_info.epsilon` 등을 사용해서 처리

   Complex number

   - `a=3-4j`

2. 문자

   - 똑같이 보이는 것도 타입이 다를수있음. type으로 형 확인 필수
   - Input()으로 받으면 무조건 ‘str’ 타입으로 받음
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

   

### 4. 연산자

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



### 5. Container

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

  - 해결방법: 새로 선언해서 해결. `b=list(a)`,`b=a[:]`

## 제어문(Control Flow)

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


