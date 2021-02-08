# CSS

Cascading Style Sheets

스타일, 레이아웃 등을 통해 **문서(HTML)를 표시하는 방법을 지정하는 언어**.

- HTML과 CSS는 각자 문법을 갖는 별개의 언어이고, 웹 브라우저는 내장 기본 스타일이 있어 CSS가 없어도 HTML이 동작함.

CSS 구문

```css
h1 { /*<- 선택자 selector */
    /* 선언 Declaration */
    /* 속성: 값 */
    color: blue;
    font-size: 15px;
}
```



#### CSS 정의 방법

- 인라인: 태그에 style 속성을 적용

  - `<div style="font-size: 50px">1</div>`

- 내부참조: head 태그에 style 속성 적용

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>My test page</title>
      <style>
          div {
            font-size: 50px
          }
      </style>
    </head>
    <body>
      <div>1</div>
    </body>
  </html>
  ```

- 외부참조

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <title>My test page</title>
      <!--외부 CSS 파일을 불러옴-->
      <link rel="stylesheet" href="mystyle.css">
    </head>
    <body>
      <div>1</div>
    </body>
  </html>
  ```

  ```css
  div {
      font-size: 50px
  }
  ```

  - 공통된 속성에 대해서 재사용 하기위해 사용함.



### CSS Selector 선택자

특정 요소를 선택하기 위해 필요한 개념

1. 기본 선택자

   ```css
   * { /* 전체 선택자 */
       color: red;
   }
   
   h2 { /* 요소 선택자 */
       color: orange;
   }
   h3,
   h4 { /* 요소 선택자, 요소 여러개를 같이 선택할수 있음*/
       font-size: 100px;
   }
   
   .green { /*클래스 선택자, */  
       color: green;
   }
   
   #purple{ /*id 선택자*/
       color: purple;
   }
   ```

   - 전체 선택자: `*`로 사용. 다른 선택자와 같이 사용할 때는 생략할 수 있음

   - 요소 선택자(타입 선택자): `typename` 로 사용. 문서 안에 있는 해당 타입의 모든 요소에 적용.
   - 클래스 선택자 `.classname`로 사용
   - 아이디 선택자 `#id`로 사용
   - 속성 선택자: `[attribute]` 로 사용. 

2. 결합자(combinarors)

   ```html
   <style>
   	/* 자식 결합자 */
       .box > p{
           font-size: 20px;
         }
       /*자손 결합자*/
       .box p{
         color:blue
       }
   </style>
   
   <div class="green box"> <!--class는 공백으로 구분-->
     <p>Lorem ipsum dolor sit, </p>
   </div>
   ```

   - 자식 결합자(child): `A > B`로 사용. 특정 요소의 바로 아래 요소를 선택함
   - 자손 결합자(하위 선택자, descendant): `A B`로 사용. 특종 요소 하위에 있는 요소를 선택함 
   - 현제 선택자: `A ~ B`로 사용. 같은 부모를 가지고 있는 요소중 A 뒤에 오는 B
   - 인접 형제 선택자: `A + B`로 사용. 같은 부모를 가지고 있는 요소 중 A 바로 뒤에 오는 B

3.  의사 클래스(Pseudo class): 필요할 때 찾아볼것

   - 링크, 동적 의사 클래스
   - 구조적 의사 클래스 



#### CSS 적용 우선순위

1. 중요도: !important
2. 우선순위
   - Inline Selector > id Selector > class Selector > element Selector(Type Selector)
3. 소스 순서
   - 우선 순위가 겹친 경우 가장 아래 작성되어 있는 것이 적용됨



#### CSS 상속

부모 요소의 속성을 자식에게 상속함. 모든 속성을 상속하진 않음

- 상속되는것: TEXT 관련 요소
- 상속되지 않는 것: box model 관련요소, position요소



### 단위

- 크기단위:

  - px: 픽셀
  - %: 부모 요소 기준 사이즈
  - em
    - 배수, 단위 요소에 지정된 사이즈에 상대적인 크기를 가짐
    - 모든 부모요소가 기준이 될 수 있음 
    - 주의할 점: 해당 부모 요소 중 em 이 있으면 중첩되어 적용됨
  - rem 
    - 최상위 요소의 사이즈(html)를 기준으로 배수 단위를 가짐
    - html의 기본 사이즈는 16px

  ```html
  <!-- em, rem 차이 -->
  <html>
  <head>
    <style>
      .em{
        font-size: 1.5em;
      }
      .rem { 
        font-size: 1.5rem;
      }
    </style>
  </head>
  <body>
    <ul class="em">
      <li class="em">1.5em</li> 	<!-- em으로 두번 상속받아서 1.5*1.5em= 36px-->
      <li class="rem">1.5rem</li> <!-- rem으로 1.5rem= 24px-->
      <li>no class</li> 			<!-- em으로 상속받아서 1.5em= 24px-->
    </ul>
  </body>
  </html>
  ```

  -  viewport 기준단위: vw, vh, vmin, vmax

- 색상 단위

  - 색상 키워드: black, white 등
  - rgb 
    - 16진수표기: `#000000` 
    - rgb함수: `rgb(0,0,0)`
  - hsl: 색상, 채도, 명도
  - a: 투명도. `rgba`,`hsla`로 사용

- css 문서 표현

  - 텍스트, 컬러,배경, 목록 꾸미기



### Box model

- margin: 테두리 바깥의 외부여백.

  - 상하좌우 설정가능

    ```css
    .margin {
        margin: 1px; 				/*상하좌우 1px*/
        margin: 1px 2px;			/*상하 1px 좌우 2px*/
        margin: 1px 2px 3px;		/*상 1px 좌우 2px 하 3px (위에서 아래로)*/
        margin: 1px 2px 3px 4px;	/*상 1px 우 2px 하 3px 좌 4px (시계방향)*/       
        /*margin-top, margin-bottom 등으로 지정할 수 있음*/
    } 
    ```

  - 마진 상쇄: 블록 요소가 위, 아래로 있는경우 마진이 겹치는 부분에서 큰 값이 적용됨.

- border: 테두리 영역.

  - 상하좌우 설정가능

- padding: 테두리 안쪽(테두리와 컨텐츠 사이)의 내부 여백.

  - 상하좌우 설정가능
  - 마진과 달리 상쇄가 없음
  - Margin과 Padding을 적절히 사용하자

- Box-sizing
  - content-box: 기본값. content를 기준으로 사이즈를 맞춤
  - border-box: border까지 합친 것을 기준으로 사이즈를 맞춤. 



## CSS Layout

### Display

HTML 요소들을 시각적으로 어떻게 보여줄지 결정하는 속성

- `display: block`
  - 화면크기 전체의 가로 폭을 가짐. 줄 바꿈 일어남
  - 블록 안에 인라인이 들어갈 수 있음
  - `div`,`ul`,`ol`,`li`,`p`,`hr`,`form` 등
  - 수평 정렬 : `margin-right: auto; margin-left: auto;`
- `display: inline`
  - 줄바꿈이 일어나지 않음
  - content 너비만큼 가로 폭 차지
  - `width`, `height`, `margin-top`, `margin-bottom` 지정 불가
  - `span`,`a`,`img`,`input`,`label` 등
  - 수평 정렬: `text-align:center;`
- `display: inline-block`
  - block과 inline 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시가능하며, block 처럼 `width`,`height`,`margin`을 지정할수 있음.
- `display: none`
  - 해당 요소를 화면에 표시하지 않음. 공간 또한 차지하지 않음
  - 비교: `visibility: hidden` 은 공간은 차지하나 화면에 표시하지 않음



### CSS Position

문서상 요소를 배치하는 방법

- `position:static`: 기준 위치(기본 값)
  - 기본적인 요소의 배치 순서에 따름(좌측 상단부터 차곡차곡)
  - 부모 요소 내에서 배치될때는 부모요소의 위치를 기준으로 배치
- `position:relative`
  - static 위치(원래 위치)를 기준으로 상대적인 위치
  - 다른 요소들에 영향을 미치지 않음
- `position:absolute`
  - static이 아닌 부모, 조상을 찾아서 기준점으로 삼음
  - 다른 요소들과 달리 새로운 규칙으로 따로 처리함
- `position:fixed`
  - 부모요소와 관계없이 브라우저를 기준으로 이동.
  - 스크롤에 상관없이 위치 고정(`viewport`에 고정)
- `position:sticky`
  - 아래로 내렸을때 일정 이상부터는 `fixed`와 비슷하게 동작
  - `fixed`와 다르게 자리를 차지함.
  - `scroll box`에 고정



### Float

- Float된 이미지의 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입된 기술
- 이미지가 아닌 다른 요소들도 적용이 되면서 웹사이트의 전체 레이아웃을 만들 수 있게 발전함.
  - 네이버 검색창 아래 메일, 카페, 블로그 있는 창
- 다른 기술이 발전되어서 다시 원래 목적으로 돌아가고있는 추세

사용예시

```css
.floatleft {
     /*none, left, right*/
    float:left; 
}
.clearfix::after{
    content: "";
    display: block;
    clear: both;
}
```

- float 설정이 없는 요소와 겹치기때문에 추가 조치 필요(`clearfix`)
  - `::after`: 가상클래스 사용 [읽어보자](https://takeuu.tistory.com/60)



### Flexbox

Flexible Box Layout. [게임 FLEXBOX FROGGY](https://flexboxfroggy.com/#ko)

요소간 공간배분과 정렬기능을 위한 **1차원(단방향) 레이아웃**

1. 요소

   - container: 부모요소
   - item: 자식요소

   - Flex Container를 조작하여 flex item을 제어한다.

2. 축

   - main axis: 메인축
   - cross axis: 교차축 . 항상 main에 수직된 방향

사용법

```css
.flexbox { /* 부모 요소에 작성 */
  display: flex;
  flex-direction: row /*defualut*/
}
```

* 배치 방향 설정: (**메인 축을 먼저 생각하자**)

  * main-axis 방향만 바뀐다
  * row: x축 정방향, row-reverse: x축 역방향,
  * column: y축 정방향(아래방향), column-reverse:  y축 역방향(위방향)

* 메인축 방향 정렬: justify으로 시작

  * `justify-content`: 메인축 기준으로 여러줄 정렬 (content: 여러줄)
  * `flex-start`(default) ,`flex-end`,`center`,`space-between`,`space-around`,`space-evenly`
  * `space-between`: 좌우정렬, 맨 끝은 마진이 없음
  * `space-around`: 균등좌우정렬, 아이템의 마진이 균등함. 맨끝의 마진은 아이템 사이사이의 마진의 반
  * `space-evenly`: 균등정렬, 맨 끝의 마진과 아이템 사이사이의 마진이 같음

* 교차축 방향 정렬: align으로 시작

  - `align`: 교차축 기준으로 정렬
    - `align-items`: Items가 한 줄
    - `align-content`: Items가 두 줄 이상 
  - `flex-start`,`flex-end`,`center`,`stretch`,`baseline`
  - `align-self`: 교차축 기준으로 선택한 요소 하나 정렬 (self: flex item 개별요소)
  - `auto`,`flex-start`,`flex-end`,`center`,`stretch`,`baseline`
  - `stretch`: container에 맞게 크기를 최대한으로 늘림
  - `baseline`: text의 base라인을 맞춰줌.

* `flex-wrap` 

  - `nowrap`: default. item이 많으면 flexbox를 넘어감
  - `wrap`:  item이 많으면 아래로 내려가면서 box안쪽에 생김
  - `wrap-reverse`: item이 많으면 위로 올라가면서 box안쪽에

* `flex-flow`: flex direction과 flex wrap 동시선언 가능. shorthand

* `order`: 개별 아이템마다 설정하면 순서를 바꿀수있음. default는 0, 음수 가능. 같은 크기면 순서대로.

* `flex-grow` default 0. 주축에서 남는 부분을 상대적 비율(grow값)로 가져감. 음수는 불가능

  - flex-grow 1 flex-grow 2 로 두개만 주어졌을때, 여백을 1:2 비율로 각각 가져감

  

### Grid

#### Bootstrap [링크](https://getbootstrap.com/)

- 반응형 그리드 시스템 one-source multi-use.
- 스타일을 좀 더 편리하게 쓸수 있게 하는 도구(based on CSS)
- 기본적인 html과 스타일이 다름. (마진이나 폰트 크기, 기본 색상 등)
  - 브라우저별로 설정이 달라서 스타일이 깨질 수 있기 때문에 CSS를 초기화함.
  - bootstrap-reboot.css로 초기화

- CDN, Content Delivery(Distribution) Network 사용
  - 컨텐츠를 효율적으로 전달하기위해 여러 노드를 가진 네트워크에 데이터를 제공하는 시스템
  - 가까운 서버를 통해 개별 유저들에게 빠르게 전달가능
  - 외부서버를 활용하므로 본인 서버의 부하가 적어짐
- 부트스트랩에 이미 만들어진 클래스를 사용하여 디자인을 적용시킴



반응형 웹

- 별도의 기술 이름이 아니라, 웹 디자인에 대한 접근 방식이나 반응형 레이아웃 작성에 도움이 되는 사례들의 모음을 기술하는데 사용되는 용어.
- 한 번의 작성으로 다양한 화면 크기에 맞는 페이지를 만들기 위해 등장함(one-source multi-use)
- Bootstrap Grid System의 display 속성을 사용하여 만들수있음 (`d-sm-none`,`d-md-block`)
  - 미디어 쿼리



#### Grid system

- Bootstrap Grid System은 flexbox로 제작됨
- **12 column**
  - 12개인 이유는  약수가 많아서 레이아웃을 다양하게 사용할수 있음
  - container, row,col로 사용
- **6 grid breakpoints**
  - xs, sm, md, lg, xl, xxl 등 여러가지 크기를 지원함
- Nesting, offset
- css grid와 다름
  - Flexbox는 1차원 레이아웃(단방향)
  - CSS Grid는 2차원 레이아웃:  X, Y 축을 따라 구성 요소를 배치
  - [비교글](https://blog.hubspot.com/website/css-grid-vs-flexbox)



