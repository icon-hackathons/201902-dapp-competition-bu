DJANGO
---
### ----------------기본 정보 ---------------------
사용 OS : Ubuntu 18.0.4
파이썬 버전 : Python 3.6.7
장고 버전 : 1.11.0
폴더 이름 : Django_Server
프로젝트 이름: mysite
앱 이름 :  crawling_App

### ----------------디렉터리 구조  ---------------------

Django_Server
├── crawling_App
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── static
│   ├── templates
│   │   └── crawling
│   │       ├── index.html
│   │       ├── realtime.html
│   │       ├── realtime_Top20.html
│   │       ├── realtime_Top20_google.html
│   │       └── realtime_google.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


### ----------------Models.py 정보  ---------------------

 #### models.py 등록된 정보

##### Receive_Naver_Data  테이블 
- Int key1 
- Char N_Word 
- Int N_Rating

def __str__(self): return self.N_Word
        
##### Receive_Google_Data 테이블
- Int key1 
- Char G_Word
- Int G_Rating

def __str__(self): return self.G_Word

##### Missing_Data 테이블
- int key1
- Char Word
- Char Type

def __str__(self): return self.Word

### ---------------- DB 정보 ---------------------
TOP20 점수 저장을 위한 데이터베이스

사용 DB : MySQl Ver 14.14 Distrib 5.7.25
기본 사용 호스트 : 127.0.0.1
기본 사용 포트 : 3306
데이터베이스 이름 : Crawling_DB  -> *DEFAULT CHARACTER SET utf8*

SQLyog으로 확인한 테이블 구조 : 

### crawling_App_receive_naver_data 

Field|Type|Collation|Null|Key|Default|Extra|Privileges|Comment
--|--|--|--|--|--|--|--|--
id|int(11)|(NULL)|NO|PRI|(NULL)|auto_increment|select,insert,update,references| - 
key1|int(11)|(NULL)|NO|-|(NULL)|-|select,insert,update,references|-         
N_Word|varchar(200)|utf8_general_ci|NO|-|(NULL)|-|select,insert,update,references|-
N_Rating|int(11)|(NULL)|NO|-|(NULL)|-|select,insert,update,references|-  

### crawling_App_receive_google_data

Field|Type|Collation|Null|Key|Default|Extra|Privileges|Comment
--|--|--|--|--|--|--|--|--
id|int(11)|(NULL)|NO|PRI|(NULL)|auto_increment|select,insert,update,references| - 
key1|int(11)|(NULL)|NO|-|(NULL)|-|select,insert,update,references|-         
G_Word|varchar(200)|utf8_general_ci|NO|-|(NULL)|-|select,insert,update,references|-
G_Rating|int(11)|(NULL)|NO|-|(NULL)|-|select,insert,update,references|-  

### crawling_App_missing_data

Field|Type|Collation|Null|Key|Default|Extra|Privileges|Comment
--|--|--|--|--|--|--|--|--
id|int(11)|(NULL)|NO|PRI|(NULL)|auto_increment|select,insert,update,references| - 
key1|int(11)|(NULL)|NO|-|(NULL)|-|select,insert,update,references|-         
Word|varchar(200)|utf8_general_ci|NO|-|(NULL)|-|select,insert,update,references|-
Type|varchar(200)|utf8_general_ci|NO|-|(NULL)|-|select,insert,update,references|-

### ----------------urls.py 정보  ---------------------

127.0.0.1:8000/					-> 	views.input
127.0.0.1:8000/realtime.html			-> 	views.index
127.0.0.1:8000/realtime_google.html		-> 	views.index2
127.0.0.1:8000/realtime_Top20.html		-> 	views.top
127.0.0.1:8000/realtime_Top20_google.html	-> 	views.top2

### ----------------views.py 정보  ---------------------

#### index
	input :     userdate = request.GET.get("userdate")
		       usertime = request.GET.get("usertime")
	output :   realtime.html, {'posts': posts, 'date': userdate, 'time':usertime, 'error':error, 'missing':missing}
 
#### index2
	input :     userdate = request.GET.get("userdate")
		       usertime = request.GET.get("usertime")
	output :    realtime_google.html, {'posts': posts, 'date': userdate, 'time':usertime, 'error':error, 'missing':missing}
 
#### top
	input :     userdate = request.GET.get("userdate")
	output :    realtime_Top20.html, {'posts': posts, 'date':userdate, 'error':error}

#### top2
	input :     userdate = request.GET.get("userdate")
	output :    crawling/realtime_Top20_google.html, {'posts': posts, 'date':userdate, 'error':error}
#### input 
	output :    crawling/index.html

## ----------------사용 방법 ---------------------
### 1.개발환경 구축
장고를 사용하게 되면 다양한 언어를 지원해주게 되는데 본 프로젝트는 파이썬을 개발코드로 선택했다
아직 파이썬이 설치되지 않았으면 먼저 아래 명령어를 통해 파이썬을 설치한다.
```shell
sudo apt install python3.6
```
설치가 완료되면 아래 명령어를 쳐서 정상적으로 설치가 되었는지 확인할 수 있다.
```shell
python3 --version
```

### 2.장고 설치
설치전에 pip이 최신버전인지 확인하다.
```shell
python3 -m pip install --upgrade pip
```
만약 오류가나서 virtualenv에 pip을 재설치 하려면 다음 명령어를 실행한다.
```shell
python -m pip install -U --force-reinstall pip
```
오류가 나지 않는다면 아래 명령어를 통해서 장고를 설치한다.
```shell
pip install django~=1.11.0
```
파이참 사용자라면 인터프리터에서 django 라이브러리를 추가해서 사용할 수 있다.

*** pip 설치시 주의사항 : 파이썬 1과 파이썬3을 잘 구분해서 설치할 것

### 3.가상환경
다음 명령어를 통해 가상환경을 생성한다
```shell
python3 -m venv myvenv
```
다음 명령어를 통해 가상환경을 실행할 수 있다.
```shell
source myvenv/bin/activate
```

>실행시키는 이유, 격리시켜서 서버에서 일어나는 동작들이 파일에 영향을 끼치지 못하게 하는 것.
>프로젝트 기초 전부를 Python/Django와 분리한다. 웹사이트가 변경되어도 개발 중인 것에 영향을 미치지 않는다.

### 4.setting.py 설정
초기 실행시 DATABASES 부분에 본인의 환경에 맞는 DB의 정보를 입력시켜야 한다.
```shell
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #데이터 베이스 엔진입력 : 현재 MYSQL엔진으로 설정됨
        'NAME': '[Input DB Name]', 	# db이름
        'USER': [Input UserName],	# 유저 이름
        'PASSWORD': [Input Password],	# 패스워드
        'HOST': '127.0.0.1',	# 아이피 정보 입력
        'PORT': '3306',		# 포트 정보 입력
    }
}
```
위 사항을 적용 시키기 위해서 mysql 안에 Crawling_DB라는 데이터베이스가 존재해야 한다.
MYsql 커맨드에서 다음 명령어를 통해서 데이터베이스를 생성
```shell
create database db_crawling character set uft8
```

### 5.변경사항 반영
아래 명령어로 모델(DB형태)이 변경되었음을 장고서버에 알려준다.
models.py 파일에서 테이블 이름과 구성을 확인하고 변경할 수 있다.
```shell
sudo python manage.py makemigrations crawling
```
그리고 아래 명령어로 모델 및 모든 변경사항을 저장한다. 
```shell
sudo python manage.py migrate crawling
```
models.py파일에 명시된 모델정보가 등록한 데이터베이스와 연동되어 테이블이 생성된 것을 확인할 수 있다.

### 6.서버 시작
manage.py 파일이 위치한 경로에서 다음 명령어 수행
```shell
python3 manage.py runserver 0.0.0.0:8000 &
```
127.0.0.1:8000 으로 접속시 정상적으로 웹이 실행 되는 것을 확인 할 수 있다.
앞에 nohup명령을 붙히면 세션을 종료하더라도 계속 서버가 돌아가게 된다.

++
다음 통하여 서버 커맨드창을 띄울 수 있다.
 ```shell
 python manage.py shell
 ```

