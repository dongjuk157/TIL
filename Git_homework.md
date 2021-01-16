# Git

1. 저장소(repository) 만들기 - git이 관리하는 폴더

   ``` shell
   $ git init
   ```

2. 파일을 스테이징하기

   ``` shell
   $ git add 파일명
   ```

3. 파일 커밋하기

   ``` shell
   $ git commit -m '커밋메시지 변경사항 요약'
   ```

   - 상태 확인하기

   ``` shell
   $ git status 
   ```

   - 정보입력(전역영역에서 commit기록 등록)

   ``` shell
   $ git config --global user.name 유저이름
   ```

   ``` shell
   $ git config --global user.email 유저이메일
   ```

4. 커밋 합치기

   ``` shell
   $ git push origin master 
   ```

   현재까지의 역사(commits)가 기록되어 있는 곳에 새로 생성한 커밋 반영

5. Branch 분기

   ``` shell
   $ git branch
   ```

   같은 작업물을 기반으로 동시에 다양한 작업을 할 수 있게 만들어 주는 기능

   독립적인 작업 영역 안에서 마음대로 소스코드를 변경할 수 있다. 분리된 작업 영역에서 변경된 내용은 추후에 기존 버전과 비교해서 새로운 하나의 버전을 만들어 낼 수 있다.

6. 원격저장소를 지정

   ``` shell
   $ git remote add origin (repo address)
   ```

   원격저장소를 지정하는데 origin이라고 하고 주소는 어디이다.

   원격저장소도 여러군데 지정가능. 이름(origin)과 주소는 다르게 써야됨

7. 원격저장소에 저장

   ``` shell	
   $ git push origin master
   ```

   origin에 master를 push한다.

## 원격(remote) 저장소

- github - 무료. ms 

- gitlab - 유료, 회사, 조직, SSAFY에서 사용

폴더(repository)단위로 관리됨

내 컴퓨터 -> github

1. 원격 저장소 repo를 컴퓨터로 다운로드.

   ``` shell
   $ git clone (repo address)
   ```

   같은 이름이 있으면 다운로드 안됨(안되는지는 모르겠는데 합쳐질거 같음)

   {.git} 폴더도 같이 생성됨.



![GitHub - qw3rtman/git-fire: Save Your Code in an Emergency](https://repository-images.githubusercontent.com/43623432/e3756280-e50c-11e9-877f-24272543fd9c)