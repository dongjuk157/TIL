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
  
-  `super()`
  
  - 부모 클래스의 내용을 사용하면서 자식 클래스에 메서드를 추가로 구현할 때 사용
  
  ```python
  class ChildClass(ParentClass):
  	def __init__(self, parent_common_value, child_only_value):# 메소드 오버라이딩 발생
          super().__init__(self,parent_common_value) 	# 상속받은 값을 사용함
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