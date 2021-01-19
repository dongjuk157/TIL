# Git 생활코딩

## 0. Git

설치하고 git bash에 다음 명령어를 입력

```shell
$ git
```

사용할수 있는 명령어들과 설명이 출력되면 제대로 설치된것.

usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

## 1. Git 1

### Git의 목적

1. 버전관리
   - 바뀔때마다 확인 가능.
   - 이전 내용과 변경 사항이 있는지 파악 가능
2. 백업
   - Local repository -> 내 컴퓨터
   - Remote repositoty -> GitHub 등. 클라우드 같은거.
   - Push: Local -> Remote; 내 파일을 원격 저장소에 밀어낸다. (저장한다.)
   - Pull: Local <- Remote; 원격 저장소의 파일을 내 폴더에 가져온다.(동기화 시킨다.)
3. 협업

## 2. Git 2

1. 버전 관리의 시작

2. 버전의 생성

   - Working Tree: 내가 일하는 공간
   - Staging Area: 버전을 만들고 싶은 파일이 있는 공간
   - Repository: 만들어진 버전

   `$ git status` 

   - Untracked files: 추적하지 않는다.

   `$ git add <file name>`

   - Staging에 올림
   - 여러 파일을 설정할수 있음

   ` $ git commit -m 'Message'`

   - repo로 옮김

   `$ git log`

   - commit 내역을 볼수있다.

   - `git log --stat`: 어떤 파일이 연결되었는지 확인가능
   - `git log -p`:이전 버전과 비교 가능(추가된 내용,파일) 

3. 버전간의 차이점 비교

   - `git diff`

4. checkout과 시간여행

5. 보충수업

6. 버전 삭제

7. 버전 되돌리기

   - `git reset --hard`:이전 버전으로 돌아갈수있음

---

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)

> clone: Clone a repository into a new directory 
>
> - 새로운 디렉토리에 repository를 복제 
> - 원격저장소에 있는 repository를 로컬 저장소에 저장하는 명령어
>
> init: Create an empty Git repository or reinitialize an existing one
>
> - 빈 Git 저장소를 만들거나 기존 저장소를 다시 초기화

work on the current change (see also: git help everyday)

> add: Add file contents to the index
>
> mv: Move or rename a file, a directory, or a symlink
>
> restore: Restore working tree files
>
> rm: Remove files from the working tree and from the index
>
> sparse-checkout: Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)

> bisect: Use binary search to find the commit that introduced a bug
>
> diff: Show changes between commits, commit and working tree, etc
>
> grep: Print lines matching a pattern
>
> log: Show commit logs
>
> show: Show various types of objects
>
> status: Show the working tree status

grow, mark and tweak your common history

> branch: List, create, or delete branches
>
> commit: Record changes to the repository
>
> merge: Join two or more development histories together
>
> rebase: Reapply commits on top of another base tip
>
> reset: Reset current HEAD to the specified state
>
> switch: Switch branches
>
> tag: Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)

> fetch: Download objects and refs from another repository
>
> pull: Fetch from and integrate with another repository or a local branch
>
> push: Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some concept guides. See 'git help <command>' or 'git help <concept>' to read about a specific subcommand or concept. See 'git help git' for an overview of the system.

***

``` shell
$ git help tutorial
```

> It is a good idea to __introduce yourself__ to Git with your name and public email address before doing any operation. The easiest way to do so is:
>
> ``` shell
> $ git config --global user.name "Your Name Comes Here"
> $ git config --global user.email you@yourdomain.example.com
> ```
>
> ###### __Importing a new project__
>
> ``` shell
> $ cd project
> $ git init
> ```
>
> git will reply
>
> ``` shell
> Initialized empty Git repository in .git/
> ```
>
> You’ve now __initialized the working directory__—you may notice a new directory created, named ".git".
>
> Next, tell Git to __take a snapshot of the contents of all files under the current directory__ (note the *.*), with *git add*: 
>
> - comma를 사용하면 현재 폴더 아래의 모든 파일들의 스냅샷을 찍음
> - 특정 파일만 하려면 add 뒤에 comma말고 파일의 이름을 적음
>
> ```shell
> $ git add .
> ```
>
> __This snapshot is now stored in a temporary staging area__ which Git calls the "index". You can permanently store the contents of the index in the repository with *git commit*:
>
> ```shell
> $ git commit
> ```
>
> 