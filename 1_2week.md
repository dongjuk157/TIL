### 개발환경 및 필요

- 파이썬 3.8.7 - 3.9는 호환성 문제가 있을수 있으므로 3.8.7로 사용
- Git - 설치후 바탕화면에서 우클릭 git bash 되는지 확인
- VScode 설치 - python, (Korean Language), git 연결

 https://www.notion.so/VS-Code-28e3c9641d1c4a88b06251e9c53f8a0c

- 텔레그램 가입
- ''파이썬챗봇'' 가입 <- 이런식의 챗봇을 만들거임



### 파이썬 

1. 변수(숫자, 문자, Boolean): 

​	ex) num=1, st='string', b=True

​	type()으로 자료형을 확인할수 있음.

​	실습: 변수활용

2. 리스트: 대괄호로 사용. 

​	ex) lst=[1,2,'st'],  lst[2]='st'

​	실습: 점심메뉴 추천

3. 딕셔너리: 중괄호로 사용. key, value 필요

​	ex) dic={'key1':'value1','key2':'value2','key3':'value3',}  dic['key2']='value2'

​	실습: 메뉴(식당)와 전화번호 알려주기

4. 조건문: if, elif, else

5. 반복문: while, for

​	for _ in range(5): pass  => 변수는 안쓰는 경우 underbar 사용.

6. Operator: 사칙연산 비교 등 있음

7. Condition: True/ False를 반환하는 식

8. 함수

   1. 내장함수:

      - 파이썬 내에서 특별한 조치 없이 사용할수 있는 함수

      - print 등

   2. 외장함수:

      - import를 사용해서 쓰는함수.

      - random, requests 등

        random.choice, random.sample

## Startcamp Day2

### API, 크롤링

1.  API
    - Application Programming Interface
    - 프로그램과 프로그램이 소통하기 위한 규칙
    - JSON: 딕셔너리 같은 형식으로 반환.
2.  크롤링
    - 실습: requests, beautifulSoup 사용

### Git

버전 관리를 위한 툴

- 버전 관리를 위해 대상이 되는 폴더가 필요함.
- 협업가능
- github, gitlab 등과 연동

명령어

- git init
  - 대상이 되는 폴더를 설정
  - 폴더당 한번만 실행. 하고 나면 (master)가 붙음
- git status
  - 현재 상태 확인
- git add [file_name] 
  - stage에 올림.  commit을 하려면 우선 수행해야 됨.
  - stage: 변경사항이 관리되는 단계
  - Untracked files - 관리 되지 않는 파일
- git commit
  - 버전을 업데이트 할수 있음
  - 제일 처음 수행하면 다음을 등록하라고 나옴
    - git config --global user.name 'your name'
    - git config --global user.email 'email'
  - git commit -m 'message'
    - commit할때마다 해당 버전의 수정사항이 무엇인지 간략하게 적어서 올림
- git log
  - 기록확인

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
- 시험때 조심! 반환(return)인지 출력(print)인지

### 서버 Server

1. Flask 
   - @App.route(‘/’): ‘/’로 들어오면 다음 함수로 연결해줌.
     - 데코레이션