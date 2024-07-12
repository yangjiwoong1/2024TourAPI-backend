# 2024TourAPI
2024 한국관광데이터공모전 팀 방방곡곡 '어서오세요'

## Rules
> 프로젝트를 진행하면서 Git Repository를 활용하는 방법, 규칙에 대한 설명

일반적으로는 아래에 설명하는 Git 명령어 순서대로 진행하면, 개발을 원활히 진행할 수 있습니다만, 특수한 경우에는 추가적인 작업을 요하기도 합니다.

코드를 사용할 때 주석에 한글 사용은 상관없으나, 디렉토리, 파일 이름, Commit Message 등 주석을 제외한 모든 항목에는 기본적으로 **영문자 및 일부 특수기호**만 사용합니다.

### Issues
> Issues는 개발 목표, 버그 제보, 개선 사항 요청 등 다양한 이슈를 제기하는 기능을 의미합니다.

Github의 본 프로젝트 Repository에 접속하고 상단의 탭 중 Issues를 클릭하면, Issues를 발행, 관리, 수정할 수 있습니다. Issues 또한 Template로 구성되어 있습니다. Template를 선택한 다음 형식에 맞춰 입력하면 됩니다.

### Pull
> Pull은 Remote Repository의 main 브랜치의 내용을 Local Repository에 받아오는 작업을 의미합니다.

```terminal
git pull
```
 위 명령어는, 현재 작업중인 폴더 (Local Repository)에 main 브랜치의 내용을 업데이트합니다. 만약, Pull 명령을 실행하지 않은 경우, 현재 Local Repository는 작업 시점에서 Remote Repository의 main 브랜치 버전과 다를 수 있으므로, 업데이트 확인 후 실행합니다.

 추가적으로, 작업중인 상태에서 Remote Repository/main 브랜치가 업데이트 된 경우 후술할 Fetch 방법을 이용하여 Conflict 상황을 해결할 수 있습니다. 하지만, 치명적인 상황이 아닌 경우, Pull Request를 통해 Conflict 부분을 Merge 과정에서 비교 후 취사선택할 수 있습니다.

### Branch
> Branch는 의미 그대로 버전의 한 가지를 의미합니다.

Remote Repository의 `main` 브랜치는 항상 최신버전을 Release하고 있습니다. `main` 브랜치의 내용은 정식 버전으로, 오류 혹은 충돌이 없는 버전으로 이루어져 있습니다. 각 파트의 사람들은 해당 `main` 브랜치에서 Local Repository로 파생시켜, 기능 혹은 버그를 추가, 수정, 삭제한 이후 `main` 브랜치로 Pull Request를 요청하고, Code Review를 통해 Merge 혹은 Close 작업을 시킵니다.

브랜치를 생성하는 것은 VSCode의 좌측 하단의 Branch 로고를 눌러 새로 생성할 수 있습니다. 일반적으로 브랜치의 이름은 `main`을 제외하고 개인의 기호대로 만들어도 무방하나, 본 프로젝트에서는 관리의 용이성을 위해 아래와 같은 규칙을 정했습니다.

```
feature/ : 새로운 기능을 추가할 때 해당 Branch 머릿말을 사용합니다.
bugfix/ : 기존 기능의 오류나 버그를 수정할 때 해당 Branch 머릿말을 사용합니다.
hotfix/ : 긴급히 수정한 내용일 경우 해당 Branch 머릿말을 사용합니다.

예시) feature/readme : readme 파일에 관련한 기능(문서 수정) 개선 작업을 한 Branch를 의미합니다.
bugfix/interface : 인터페이스 구성 요소 중 발생한 버그를 수정한 작업을 포함한 Branch를 의미합니다.
hotfix/20240701 : 2024-07-01에 긴급히 수정한 Branch를 의미합니다.

위의 예시와 같이, 머릿말 이후에는 최대한 간결하게 자신의 작업을 설명하는 영단어를 사용합니다. 이때 한국어는 *절대* 사용하지 않습니다.
```

위의 Pull 작업을 실행한 이후, Local Repository에서 Branch를 생성해야 비로소 작업환경이 마련됩니다. 이후에는 원하는 기능을 추가, 수정, 삭제 등 자유롭게 작업해주시면 됩니다!

#### 스태이징 (Staging)
현재 Local Repository에서 수정한 파일 중, 커밋할 파일을 지정하는 작업을 의미합니다.

```terminal
git add ./test/test.c
```
위 명령어로 정해진 파일을 스태이징 할 수 있습니다만, 후술할 VSCode의 기능을 활용해 하는 것을 권장합니다.

VSCode에서는, 좌측 메뉴 바의 3번째 탭을 통해 변경 사항을 추적하고, 스테이징 / Commit 을 쉽게 GUI를 통해 조작할 수 있습니다. 명령어를 사용한 Git 버전 관리가 이후에는 유용하지만, 당장은 GUI를 사용하여 실수를 줄이도록 합시다.

### Commit
> Commit이란, 로컬 작업 내용을 저장하기 위해 사용합니다.

```terminal
git commit -m "Commit Message"
```
 위 명령어는 현재 스태이징한 파일들을 커밋하고, 이때의 커밋 메시지를 선언합니다. 커밋 메시지란, 커밋 내용을 알려주는 메시지로 현 프로젝트에서는 정해진 양식에 따라 사용하고 있습니다. 따라서 정해진 양식에 맞춰 일목요연하고 간단하게 서술하는 것이 필요합니다.

 Commit Message는 이미 Template으로 구현되어 프로젝트 파일에 포함되어 있습니다. VSCode의 Commit 기능을 수행한다면, 화면에 정해진 양식이 출력되는데, 이때 **제거하라는 주석**을 제거한 이후 양식에 맞춰 입력해주시면 됩니다.

 그러나 Template을 개인 Local Repository에 적용하기 위해서는 아래 명령어를 **프로젝트 폴더** 터미널에서 입력해줘야 합니다.

 ```
 git config commit.template ./.github/.gitmessage.txt
 ```

### Branch 발행 (Push)
> 자신의 전체 작업을 마치셨다면, Remote Repository에 자신이 개발한 Branch를 발행해야 합니다.

```
git push origin/main 브랜치 이름
```
위 명령어를 사용할 수 있으나, 위의 설명과 마찬가지로 VSCode 상의 GUI 기능을 활용하는 것을 추천합니다. 이제 `main` 브랜치에 올리기까지 한 단계만 남았습니다!

### Pull Request 발행
> Branch를 Remote Repository에 발행하였다면, Remote Repository에서 Pull Request (PR)를 발행할 수 있습니다.

Remote Repository (Github)에 인터넷 브라우저를 통해 접속합니다. 현 프로젝트 Repository에 들어오면 **자신이 발행한 Branch**로 구성되어 있는 Pull Request 발행 버튼을 클릭합니다.

Pull Request 또한 Template으로 구성되어 있습니다. 양식에 맞춰 신중히 작성하고 **우측의 Reviewers, Assignees, Labels**까지 선택한 다음 발행합니다.

다른 구성원들의 Code Review 이후 문제가 없다고 판단된다면, Merge 기능을 실행하고 Remote Repository에서 해당 Branch를 제거하면 최종적으로 `main` 브랜치에 자신의 작업물이 업로드되었습니다!