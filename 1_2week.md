### 개발환경 및 필요

- 파이썬 3.8.7 - 3.9는 호환성 문제가 있을수 있으므로 3.8.7로 사용
- Git - 설치후 바탕화면에서 우클릭 git bash 되는지 확인
- VScode 설치 - python, (Korean Language), git 연결

 https://www.notion.so/VS-Code-28e3c9641d1c4a88b06251e9c53f8a0c

- 텔레그램 가입
- ''파이썬챗봇'' 가입 <- 이런식의 챗봇을 만들거임



### 파이썬 

1. 변수(숫자, 문자, Boolean): 
   - `num=1`, `st='string'`, `b=True`
   - `type()`: 자료형 확인

2. List
   - `lst=[1,2,'st']`,  `lst[2]='st'`

3. 딕셔너리: 
   - 중괄호로 사용. key, value 필요
   - `dic={'key1':'value1','key2':'value2','key3':'value3',}`  
   - `dic['key2']='value2'`

4. 조건문: if, elif, else
5. 반복문: while, for
   -  `for _ in range(5): pass`  => 변수 안쓰는 경우 underbar 사용.

6. Operator: 사칙연산 비교 등 있음

7. Condition: `True`/ `False`를 반환하는 식

8. 함수

   1. 내장함수:

      - 파이썬 내에서 특별한 조치 없이 사용할수 있는 함수

      - print 등

   2. 외장함수:

      - import를 사용해서 쓰는함수.

      - random, requests 등

        random.choice, random.sample

### API, 크롤링

1.  API
    - Application Programming Interface
    - 프로그램과 프로그램이 소통하기 위한 규칙
    - JSON: 딕셔너리 같은 형식으로 반환.
2.  크롤링
    - 실습: requests, beautifulSoup 사용

### 챗봇 

1. 텔레그램
   - BotFather 사용
     - api 문서 있으니 참고
     - `https://api.telegram.org/bot<token>/METHOD_NAME `
     - /newbot
     - `METHOD_NAME: getUpdate`:
     - `METHOD_NAME: sendMessage`:  chat_id, message 필요
2. 서버에 올려서 24시간 돌릴수 있음
   -  Aws, MS azure같은곳
   - pythonanywhere : 다루기 쉽게 만든 2차 서비스 
3. Naver API(developers.naver.com)
   -  필요
     - Client id
     - Client secret
   - 파파고 api(실습: papago.py)
     - api를 사용할 때 headers가 필요하고 요청하는 방법은 api마다 다름
     - 초월번역 가능하다 했는데 잘 안됨 ㅠ
   - 검색 api

### 함수 Function

- 편하게 쓰려고 사용
- 함수안에서 발생한 값이 필요한 경우 return으로 반환

### 서버 Server

1. Flask 
   - @App.route(‘/’): ‘/’로 들어오면 다음 함수로 연결해줌.
     - 데코레이션