# 어렵다어려워



뭔가 잘못 삭제해서 `git push` 도 안되고...

hint로  `git pull` 하라고나오는데 뭔지 잘 모르겠고

그래서 그냥 강제로 `git push origin +master` 했다

---

``` shell
 warning: LF will be replaced by CRLF 
The file will have its original line endings in your working directory
```

이렇게 뜬 이유는 나는 윈도우를 쓰고 있는데 git bash로 텍스트 파일을 저장해서 문제가 생긴것이다.

자세한 내용이 궁금하면 다시 찾아보도록 하자.

https://blog.jaeyoon.io/2018/01/git-crlf.html

https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important

해결 하는 방법

``` shell
$ git config --global core.autocrlf true
```

뭐지 자꾸뜨는데;;

warning이라 그냥 무시하고 사용해도 상관없다

---

#### 로컬과 git 저장소에서 파일 삭제하는 방법

##### 1. 로컬 디렉토리와 git에서 모두 삭제하는 방법

`git rm <file_name or folder_name>` 

##### 2. git 에서만 삭제하는 방법

`git rm --cached <file_name>`

둘다 진행하고 커밋해줘야 적용된다.

