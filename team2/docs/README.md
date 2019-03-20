<<<<<<< HEAD
# Without doubt Project
## 개요
Without Doubt Project는 Naver, Google의 실시간 검색어를 Crawling해서, ICON Project의 Loopchain 환경에 데이터를 저장하고, 웹에서 지난 실시간 검색어 검색과 검색어의 추이를 확인하여 검색어 트랜드를 확인하는 서비스를 개발한다.

## 구성도
![54107716-47bfc000-441d-11e9-8ee1-29e87e614749.JPG](https://user-images.githubusercontent.com/47471638/54107716-47bfc000-441d-11e9-8ee1-29e87e614749.JPG)
<br>
## t-bears 설치 방법 및 설명
- [GitHub - icon-project/t-bears: Test suite for ICON SCORE development](https://github.com/icon-project/t-bears)
## Crawler
### 크롤링 하기전 필수 요소
- 구글드라이버
- python3

- NAVER
```shell 
pip install bs4
```
  
- GOOGLE
```shell
pip install bs4
pip install selenium
   
http://chromedriver.chromium.org/downloads 해당 사이트에 접속하여 
자신 크롬브라우저 버전에 해당하는 chromedriver를 다운받아준다
   
해당 파일은 zip이므로 unzip 해준다
만약 unzip이 없을경우
   
apt-get install unzip 
    
unzip 집이름.zip
   
```

 ###  ** 압축해제한 chromedriver경로를 알아야 chromedriver를 사용 할 수 있다
  
<br>

## DataBase
- mysql 설치
```shell
sudo apt-get install mysql-server
```
- mysql 실행
```shell
sudo mysql -u root -p
```
- mysql 데이터베이스 생성
```shell
create database 'DB명' character set uft8
```
- mysql 계정생성
```shell
create user '계정아이디'@'%' identified by '비밀번호';
# '%'를 입력해주면 외부에서의 접속을 허용하게 된다.
```
- mysql 계정권한 부여
```shell
grant select privileges on 'DB명'.'테이블명' to '계정명'@'%' identified by '계정비밀번호'
#권한 적용
flush privileges;
```
- pymysql 설치
MySql 외부에서 DB에 접속하기 위해서 pymysql 라이브러리 설치
```shell
pip install pymysql
```

<br>

## Django
### 가상환경
- 가상환경 설치
```shell
python3 -m venv myvenv
```
- 가상환경 실행
```shell
source myvenv/bin/activate
```

### 장고 설치
- 장고 설치
```shell
pip install django~=1.11.0
```
### 장고 설정
- setting.py파일에서 DB부분을 자신의 환경과 맞게 설정해준다.
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

- 모델(DB형태)이 변경되었음을 장고서버에 알려줌
```shell
sudo python manage.py makemigrations crawling
```
- 모델 및 모든 변경사항 저장
```shell
sudo python manage.py migrate crawling
```
### 장고 실행방법
```shell
nohup python manage.py runserver 0.0.0.0:8000 &
```
- 웹페이지 접속
127.0.0.1:8000 으로 접속시 정상적으로 웹이 실행됨

=======
When will we complete it?
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774

