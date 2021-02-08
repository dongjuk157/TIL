# HTML

Hyper Text Markup Language

- Hyper Text
  - 사용자에게 내용의 비순차적 검색이 가능하도록 제공되는 텍스트.
  - 문서 내의 특정한 단어가 다른 단어나 데이터베이스와 링크되어 있어 사용자가 관련 문서를 넘나들며 원하는 정보를 얻을 수 있음.
  - HTTP : Hyper Text Transfer Protocol
- Markup Language
  - 웹페이지를 작성하기 위한 언어.
  - 태그 등을 이용해서 웹 페이지와 컨텐츠(문서, 데이터 등)의 구조를 정의함.
  - 프로그래밍 언어와는 다르게 단순히 데이터를 표현함
- 웹 표준 - W3C, WHATWG -> WHATWG



### HTML 기본구조

```html
    <!--Attribute-->
<p class="editor-note">   <!--The opening tag-->
    My cat is ver grumpy. <!--content-->
</p>                      <!--The closing tag-->
<!------------------ Element ------------------>
```

- The opening tag, 여는 태그: 요소의 이름으로 구성되고, 요소가 시작되는 곳이다.
- The closing tag, 닫는 태그: 여는태그와 같지만 슬래시가 포함되고, 요소의 끝을 나타낸다.
  - 닫는 태그를 쓰지 않으면 의도하지 않은 결과가 나타날 수 있음.
- The content 컨텐츠: 요소의 내용
- The element 요소: 여는태그, 닫는태그, 컨텐츠로 이루어진 것.

- Attributes 속성: 실제 컨텐츠로 표시되지 않는 추가적인 정보. 필수적인 요소는 아님
  - html 스타일 가이드 - 따옴표 대신 쌍따옴표 사용. 공백은 사용하지 않는다.(구분할때만 사용)



```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="My test image">
  </body>
</html>
```

- `<!DOCTYPE html>`
  - 기본적으로 문서가 올바르게 작동하는지 확인하는 데만 필요함
- `<html>` 
  - HTML 문서의 최상위 요소. root요소 라고도함.
- `<head>`
  - 문서 제목, 문자코드와 같이 문서의 정보를 담고 있음. CSS선언 혹은 외부 로딩파일 지정 등도 작성
  - **브라우저에 나타나지 않음**. 
  - OG, Open Graph Protocol: HTML 문서의 메타 데이터를 통해 문서의 정보를 전달. 메타 태그사용 `<meta property="og:title">`
- `<body>`
  - **브라우저 화면에 나타나는 정보**



DOM 트리, Document Object Model 

- 부모 형제 관계를 나타내는 트리
- 문서의 각 부분들을 객체로 표현한 API



Semantic Tag 시맨틱 태그: **의미론적 요소**를 담은 태그

- HTML5에서  `<div>`와 같은 동작을 하지만 의미를 담은 태그가 등장. 

- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미있는 정보를 표현

  - SEO(검색엔진 최적화)를 위해서 메타, 시맨틱 태그등을 통한 마크업을 효과적으로 해야함.

- 대표적인 시맨틱 태그

  - `<header>`: 문서 전체나 섹션의 헤더(머리말부분)
  - `<nav>`: 내비게이션
  - `<aside>`:사이드에 위치한 공간, 메인콘텐츠와 관련성이 적은 콘텐츠
  - `<section>`: 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - `<article>`: 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `<footer>`: 문서의 전체나 섹션의 푸터(마지막부분)
  - 이외에도 `<details>`, `<figcaption>`, `<figure>`, `<main>`, `<mark>`,`<summary>`, `<time>` 등이 있음
  - `<h1>`, `<table>`, `<a>`, `<form>`은 시맨틱태그로 볼 수 있으나 HTML5 이전부터 있었음.

- Non-semantic tag: `<div>`, `<span>`

  ```html
  <!--non-semantic-->         <!--semantic-->
  <div>				<!----> <header>
    <div></div>		<!---->	  <nav></nav>
  </div>				<!----> </header>
  <div>				<!----> <section>
    <div></div>		<!---->   <article></article>
    <div></div>		<!---->   <article></article>
  </div>				<!----> </section>
  <div></div>			<!----> <footer></footer>
  ```

- 시맨틱 웹: 메타 데이터를 부여하여, 의미와 관련성을 가지는 거대한 데이터베이스로 구축하고자 하는 발상



### HTML 문서 구조화

많은 태그들이 있으나 필요할때 찾아서 사용

- 그룹 컨텐츠 
  - `<p>`: paragraph, 하나의 문단을 만들때 사용
  - `<hr>: ` 수평선
  - `<ol>`: ordered list, `<ul>`: unordered list
  - `<pre>`: 미리 정의된 형식(preformatted)의 텍스트를 사용
    - 텍스트에 사용된 여백과 줄바꿈이 모두 그대로 브라우저 화면에 나타남
    - 독특한 서식의 텍스트나 컴퓨터 코드 등을 HTML 문서에 표현가능
  - `<blockquote>`:  텍스트가 긴 인용문
  - `<div>`: block 속성
- 텍스트 관련
  - `<a>`: 하이퍼링크를 걸어주는 태그. 여러 속성을 사용함
  - `<b>`: 그냥 굵게, `<strong>`굵게 + 의미 강조(sementic)
  - `<i>`: 이탤릭,`<em>`:이탤릭 + 의미 강조(sementic)
  - `<span>`:  inline 속성
  - `<br>`: 줄 바꿈
  - `<img>`: 이미지
- table: 표 
- form: 서버에서 처리될 데이터를 제공하는 역할
  - 기본 속성: action, method 
- input: 다양한 타입을 가지는 입력 데이터 필드
  - input요소의 동작은 type에 따라 달라짐.

