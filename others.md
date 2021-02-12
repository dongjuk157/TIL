## Emmet

HTML & CSS를 작성할 때, 마크업을 빠르게 작성하기 위해 사용되는 오픈 소스

단축키, 약어등을 사용함

- `.classname`, `#id`같은 자동완성
- `div>ul>li*4` 자식관계
- `div> ul +ol` 형제관계
- `li*4{$}` 번호 자동 붙이기

자동완성 탭 안뜨는 경우 ctrl+space로 다시 활성화 시킬수있음(vscode)



## 파일경로

1. 절대 경로: 찾고자 하는 파일의 절대적 위치 

    `C:\Users\Home\Desktop\folder\file.txt`

2. 상대 경로: 현재 파일을 기준으로 어디에 있는지 기입하는 방식

   `..\programs\kakaotalk.lnk` => `..\ `: `C:\Users\Home\Desktop`

   - `..`: 상위 폴더
   - `.`: 현재 폴더
   - `~`: 홈 디렉토리



### API, 크롤링

1.  API
    - Application Programming Interface
    - 프로그램과 프로그램이 소통하기 위한 규칙
    - JSON: 딕셔너리 같은 형식으로 반환.
2.  크롤링
    - 실습: requests, beautifulSoup 사용



### 챗봇 

1. 텔레그램

   - 파이썬챗봇 같은 거 

   - BotFather 사용
     - api 문서 있으니 참고
     - `https://api.telegram.org/bot<token>/METHOD_NAME `
     - /newbot
     - `METHOD_NAME: getUpdate`:
     - `METHOD_NAME: sendMessage`:  chat_id, message 필요

2. 서버에 올려서 24시간 돌릴수 있음

   -  Aws, MS azure같은곳
   -  pythonanywhere : 다루기 쉽게 만든 2차 서비스 

3. Naver API(developers.naver.com)

   -  필요
      - Client id
      - Client secret
   -  파파고 api(실습: papago.py)
      - api를 사용할 때 headers가 필요하고 요청하는 방법은 api마다 다름
      - 초월번역 가능하다 했는데 잘 안됨 ㅠ
   -  검색 api



### 서버 Server

1. Flask 
   - @App.route(‘/’): ‘/’로 들어오면 다음 함수로 연결해줌.
     - 데코레이션