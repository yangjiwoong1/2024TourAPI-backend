# 장고 설치 및 설정 방법

## 가상환경

### 가상환경 생성
파이썬 프로젝트를 위해선 개인마다 로컬 컴퓨터에 파이썬 가상환경을 생성해야 한다. 자세한 설정 과정은 os마다 다르므로 따로 기술하지 않겠다. 개요는 Linux, macOS를 기준으로 다음과 같이 기술하였다.
+ python 버전: 3.12.4
  + 해당 버전의 파이썬 인터프리터로 **backend 디렉토리 아래** 가상환경(venv)을 추가한다.
    + 파이썬 버전 확인은 $ python --version을 통해 가능하다.
  + (backend dir) $ python3 -m venv venv

### 가상환경 활성화
+ 파이썬 가상환경은 프로젝트에 필요한 패키지나 라이브러리 등을 시스템 환경에 격리하여 관리한다. 따라서 장고 프로젝트 실행 전 항상 가상환경을 활성화 해주어야 한다. 가상환경이 활성화됐는지 확인하는 방법은 터미널 상의 오른쪽에 가상환경 표시가 뜬다. 잘 모르겠으면 인터넷을 찾아보도록 하자.
  + 활성화: (backend dir) $ source venv/bin/activate
  + 비활성화: $ deactivate
  
## requirements.txt
requirements.txt 파일은 현재 프로젝트에 설치된 파이썬 패키지를 관리한다. 가상환경을 활성화 한 상태로 다음 명령어를 통해 필요한 파이썬 패키지를 내려받을 수 있다. git pull 명령어를통해 원격 저장소의 변경 사항을 로컬에 가져온 뒤, 환경이 변경되었을 수 있으므로 항상 다음 명령어를 실행해주자.
+ $ pip install -r requirements.txt

## Django 개발 서버 실행
backend dir에서 순서대로 다음 명령어를 통해 Django 내장 개발 서버를 실행할 수 있다(가상환경 활성화는 기본이다.). localhost:8000에서 실행된다.
+ (backend dir) $ python manage.py migrate
+ (backend dir) $ python mange.py runserver

# 개발 시 주의 사항
장고 백엔드 개발자는 다음과 같은 사항을 주의해야 한다.
+ "pip install 명령어"로 패키지를 설치한 후엔 항상 backend dir에서 "pip freeze > requirements.txt" 명령어를 통해 패키지 의존성을 업데이트 해주어야 한다.
+ 두 명 이상이 동시에 모델 수정 후 "makemigrations"을 실행하면 merge conflict가 발생할 가능성이 높다. 모델 스키마를 변경할 일이 있으면 사전에 상의 하자.