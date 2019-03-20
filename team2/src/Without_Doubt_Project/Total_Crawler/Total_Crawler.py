<<<<<<< HEAD
﻿#-----------------------------------------crawling----------------------------------------------
=======
#-----------------------------------------crawling----------------------------------------------
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
import requests, time, datetime
from bs4 import BeautifulSoup
from selenium import webdriver


#---------------------------------------db connect----------------------------------------------
import pymysql
<<<<<<< HEAD
from pytz import timezone

#---------------------------------------Icon SCORE Service--------------------------------------
import json
# SCORE's Dictionaty DB does not support List format, so we change the List format to JSON format
=======


#---------------------------------------Icon SCORE Service--------------------------------------
import json
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.wallet.wallet import KeyWallet

<<<<<<< HEAD

#---------------------------------------Icon SerFvice rink---------------------------------------
icon_service = IconService(HTTPProvider("https://ctz.solidwallet.io/api/v3"))
# 아이콘 서비스 어느 주소단이랑 연동할 것인가
_score_address = "cx~~~~~~~"
# Deployed SCORE Address
_keystore_address = "hx~~~~~~~"
# The address of the wallet that will trigger the transaction
wallet = KeyWallet.load("key's full path", "key's password")
# 

=======
'''
#time check
t = time.time()
now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(t))
with open('/home/lyu/PycharmProjects/Without_Doubt_Project/Total_Crawler/log.txt', 'a+') as f:
    f.write(now+"\n")
'''


#---------------------------------------Icon Service rink---------------------------------------
icon_service = IconService(HTTPProvider("http://127.0.0.1:9000/api/v3"))
_score_address = "cxd8477e0e67273112e64ed81ab5b578bb4f997da6"
_keystore_address = "hx055ca4808e82f7c0e4eafa884cefcfec15e8387b"
wallet = KeyWallet.load("./mykeystore", "1q2w3e4r!")
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774


#-------------------------------------------Main source------------------------------------------
class calltransaction_transaction_RT():
<<<<<<< HEAD
#python 내에 calltransaction_transaction_RT 이라는 클래스를 선언해준다.
	start_time = time.time()
	#시작시간을 측정하기위해 만듦 start_time변수 안에 time함수를 사용하여 시간을 저장
	
	now = datetime.datetime.now()
	#now라는 변수안에 현재 날짜와 시간을 대입
	nowDate = now.strftime('%Y%m%d')
	#nowDate 현재 날짜를 구분하기위해 변수선언한후 now변수에 저장된 시간들을 갖고오는데 %년%월%일만 가져와서 저장
	nowTime = now.strftime('%H%M')
	#nowTime에 현재시각을 대입하기위해 %시간 %분을 대입해준다
	
	html = requests.get('https://www.naver.com/').text
	#html이란 변수에 beautifulsoup을 사용하여 요청하여 얻어온다 naver를 text형식으로
	soup = BeautifulSoup(html, 'html.parser')
	#무엇을이 여기서 결정된다 soup에 beautifulsoup을 사용하여 html에 저장된 것을 parser해온다
	#parser란 구문분석이란 의미로 인터넷소스들을 끌어온다
	title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
	#title_list안에 soup에 저장된 값들중에 select 선택하겠다. ()안의 값들만 골라오겠다 
	#()안의 값은 네이버소스에서 직접검색하면 찾아볼수 있다.
	
	Machined_title_list = list()
	#Machined_Google_title_list라는 리스트를 선언해준다
	for idx, title in enumerate(title_list, 1):
	    Machined_title_list.append(title.text)
	#for문에 idx(순서)와 title(새로운변수)을 돌리는데 enumerate(숫자를세다) title_list를 
	#그리고 그값을 Machined_Google_title_list에 하나씩 append}(리스트에 삽입시킨다 title.text를)
	naver_list=Machined_title_list[0:5]
	#네이버 순위를 5개만 갖고오기 위한 작업
	print(naver_list)
	
	params = {
	    "_date": nowDate,
	    "_time": nowTime,
	    "_div": 'NAVER',
	    "_value": json.dumps(naver_list)
	}
	#params 란 스코어와 sdk관계에서 값들을 넘겨줄 매게변수를 설정해주는 값을 정해줄 수 있는 것 이라고 생각하면쉽다
	#그렇기에 키값으로 들어갈 것들과 위에서 리스트로 정리할 값을 json 형식으로 묶어서 보낸다
	transaction = CallTransactionBuilder() \
	    .from_(_keystore_address) \
	    .to(_score_address) \
	    .step_limit(10_000_000) \
	    .nid(1) \
	    .nonce(100) \
	    .method("transaction_RT") \
	    .params(params) \
	    .build()
	#스코어와 연동시킬 CallTransactionBuilder()를 transaction에 넣을건데 그밑의 값들을 넣을 것이다 라는 의미이다.
	
	'''
	
	    from_ : 거래를 수행하는 지갑 주소. 기본 주소는 귀하의 계정 주소입니다.
	    to : 거래를 받기 위해 동전이나 SCORE 주소를받는 지갑 주소
	    step_limit : 트랜잭션 처리를위한 최대 단계 값
	    nid : 네트워크 ID. 값을 설정하지 않으면 기본 nid는 1입니다. (주망 1 등)
	    nonce : 트랜잭션 해시 충돌을 방지하는 데 사용되는 임의의 숫자
	    method : SCORE의 메소드
	    params : SCORE 메서드에 전달 된 매개 변수입니다. 매개 변수의 데이터 유형은 dict 여야합니다 . (선택 과목)
	    버전 : 프로토콜 버전 (V3의 경우 3). 값을 설정하지 않은 경우 기본 버전은 3입니다.
	    timestamp : 트랜잭션 생성 시간. 시간 소인은 마이크로 초입니다. 값을 설정하지 않으면 기본 타임 스탬프가 설정됩니다.
	    Build : 호출 트랜잭션 객체를 반환합니다.
	'''
	
	
	#print(nowDate, nowTime, 'NAVER') 
	signed_transaction = SignedTransaction(transaction, wallet)
	#SignedTransaction(transaction: Transaction, wallet: Wallet)
	#transaction : 아직 서명 필드가없는 트랜잭션 객체
	tx_hash = icon_service.send_transaction(signed_transaction)
	
	# print(tx_hash)
	time.sleep(5)
	# tx_result = icon_service.get_transaction_result(tx_hash)
	# print(tx_result['status'])
	#print("--- %s seconds ---" % (time.time() - start_time))
	
	#---------------------------------------------GOOGLE----------------------------------------
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	#위의 옵션들은 selenium을쓸때 아래에서 구글브라우저를 열때 자동으로 닫히게 해주는 옵션들이다 이외에 다른옵션들도 많다
	path = "chromedriver's full path"	
	#이전에 chromedriver을 압축해제한 곳의 경로를 path 변수에 저장시킨다
	driver = webdriver.Chrome(path, chrome_options=options)
	time.sleep(5)
	#dirver 안에 path라는 경로에 있는 크롬 웹드라이버를 대입
	driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all")
	#driver.get("url") 구글 개발자모드안에 소스에서 xpath로 검색해오면 된다. 위 드라이브로 get 얻어오겠다 가로안의 url 의 값을
	time.sleep(5)
	
	req = driver.page_source
	#req안에 driver로 얻어온 page_source를 넣어준다
	
	soup = BeautifulSoup(req, 'html.parser')
	#soup안에 Beautifulsoup으로 (req에 저장된 값을 파싱시킨다 html.parser)
	
	title_list = soup.select('div > span:nth-child(1) > a')
	#셀레니움 드라이버 종료 
	driver.quit()

	'''
	그리고 title_list에 soup안에 저장내용중에 select 선택해온다
	(div > span:nth-child(1) > a) 
	자신이 갖고오고 싶은 소스 값들을 개발자모드에서 selector 해오면
	해당값들이 복사되어 온다
	'''
	
	Temp_list = title_list[0:5]
	Machined_Google_title_list = list()
	
	for title in Temp_list:
	    Machined_Google_title_list.append(title.text.strip())
	print(Machined_Google_title_list)
	params_G = {
	    "_date": nowDate,
	    "_time": nowTime,
	    '_div': 'GOOGLE',
	    "_value": json.dumps(Machined_Google_title_list)
	}
	transaction_G = CallTransactionBuilder() \
	    .from_(_keystore_address) \
	    .to(_score_address) \
	    .step_limit(10_000_000) \
	    .nid(1) \
	    .nonce(100) \
	    .method("transaction_RT") \
	    .params(params_G) \
	    .build()
	#print(nowDate, nowTime, 'GOOGLE')
	signed_transaction_G = SignedTransaction(transaction_G, wallet)
	tx_hash_G = icon_service.send_transaction(signed_transaction_G)
	#send_transaction(signed_transaction: SignedTransaction)
	#트랜잭션을 보냅니다.
	#print("--- %s seconds ---" % (time.time() - start_time))
	#------------time sleep-------------------------------------
	# print(tx_hash_G)
	# time.sleep(10)
	# tx_result_G = icon_service.get_transaction_result(tx_hash_G)
	# print(tx_result_G['status'])
	
	# ------------------------Google DB Con------------------------
	

	# MySQL Connection 연결
	conn = pymysql.connect(host='127.0.0.1', user='admin', password='rootroot',
	                       db='Crawling_DB', charset='utf8')
	
	#DB접근을 위한 기능을 객체화 한다, 뒤에 pymysql.cursors.DictCursor은 변수를 통해 동적으로 할당해주기 위한 옵션이다.
	curs = conn.cursor(pymysql.cursors.DictCursor)
	
	#5점 부터 1점까지 차례대로 점수를 부여하기 위해 b라는 변수 선언
	b = 5
	
	# 가지고온 현재 1등 데이터가 TOP20 테이블에 이미 존재하고 있는지 검사 (없다면 누락값을 의심해 볼 수 있음)
	# 가지고온 현재 1등 데이터를 check라는 변수에 할당한다.
	check = Machined_Google_title_list[0]
	#crawling_App_receive_google_data라는 테이블에서 key1 칼럼이 변수 nowDate 값과 일치하고 G_Word 칼럼이 check와 일치하는 값을 가지고 온다
	sql = "select * from crawling_App_receive_google_data where key1=%s and G_Word=%s"
	curs.execute(sql, (localnowDate, check))
	check_resuit = curs.fetchall()
	print(check_resuit)

	#만약 데이터가 테이블에 존재하지 않으면 missing_data테이블에 값을 입력해준다. (누락값으로 의심되는 값을 의미)
	if not check_resuit and int(nowTime) != 0:
	    sql = "INSERT INTO crawling_App_missing_data (key1,Word,type) VALUES(%s,%s,'G')"
	    curs.execute(sql, (localnowDate, check))
	    rows = curs.fetchall()
	    conn.commit()
	
	# 가져온 20개의 키워드 insert 또는 update
	# 첫번째 키워드 부터 스무번째 키워드 까지 순서대로 수행
	for a in Machined_Google_title_list:
	
	    #insert할지 update할지 구분을 위해 검색된 단어의 점수 존재 여부를 체크하고, 몇점인지 확인한다.
	    #crawling_App_receive_google_data라는 테이블에서 key1 칼럼이 변수 nowDate 값과 일치하고 G_Word 칼럼이 a와 일치하는 값의 G_Rating를 가져온다.
	    #조건절에 nowDate 옵션을 주어서 현재 날짜에 있는 데이터로 범위를 제한한다.
	    sql = "select G_Rating from crawling_App_receive_google_data where key1=%s and G_Word=%s"
	    curs.execute(sql, (localnowDate, a))
	    num = curs.fetchall()
	
	    #만약 G_Word 값이 존재한다면 
	    if num:
	        # print("already exist")
	#DB에서 가져온 데이터의 첫번째 키워드 부터 스무번째 키워드 까지 순서대로 수행
	#기존의 점수 값에서 점수를 더해주는 기능
	        for x in num:
	            d = list(x.values())
	            k = int(d[0])
	            k = k + b
	            # 만약 a[0]값이 crawling_receive_google_data에 없으며 주의 메세지 출력
	
	#crawling_App_receive_google_data라는 테이블에서 G_Word 칼럼이 a와 일치하는 값의 G_Rating을 k변수로 업데이트 한다.
	            sql = "UPDATE crawling_App_receive_google_data SET G_Rating=%s WHERE G_Word=%s"
	            curs.execute(sql, (k, a))
	            rows = curs.fetchall()
	            conn.commit()
	
	#만약 G_Word 값이 존재하지 않는다면
	    else:
	        # print("New Input")
	#crawling_App_receive_google_data라는 테이블에서 새로운 레코드를 생성한다.(key1 : localnowDate, G_Word : a, G_Rating : b)
	        sql = "INSERT INTO crawling_App_receive_google_data (key1,G_Word,G_Rating) VALUES(%s,%s,%s)"
	        curs.execute(sql, (localnowDate, a, b))
	        rows = curs.fetchall()
	        conn.commit()
	#키워드 순위가 떨어지면 점수도 1점씩 작게 부여하기 위해서 b에서 1을 뺀다.
	    b = b - 1

	# ------------------------Naver DB Con------------------------
	#5점 부터 1점까지 차례대로 점수를 부여하기 위해 b라는 변수 선언
	b=5
	
	# 가지고온 현재 1등 데이터가 TOP20 테이블에 이미 존재하고 있는지 검사 (없다면 누락값을 의심해 볼 수 있음)
	# 가지고온 현재 1등 데이터를 check라는 변수에 할당한다.
	check = naver_list[0]
	#crawling_App_receive_naver_data라는 테이블에서 key1 칼럼이 변수 nowDate 값과 일치하고 N_Word 칼럼이 check와 일치하는 값을 가지고 온다
	sql = "select * from crawling_App_receive_naver_data where key1=%s and N_Word=%s"
	curs.execute(sql, (localnowDate, check))
	check_resuit = curs.fetchall()
	
	#만약 데이터가 테이블에 존재하지 않으면 missing_data테이블에 값을 입력해준다. (누락값으로 의심되는 값을 의미)
	if not check_resuit and int(nowTime) != 0 :
	    sql = "INSERT INTO crawling_App_missing_data (key1,Word,type) VALUES(%s,%s,'N')"
	    curs.execute(sql, (localnowDate, check))
	    rows = curs.fetchall()
	    conn.commit()
	
	# 가져온 20개의 키워드 insert 또는 update
	# 첫번째 키워드 부터 스무번째 키워드 까지 순서대로 수행
	for a in naver_list:
	
	#insert할지 update할지 구분을 위해 검색된 단어의 점수 존재 여부를 체크하고, 몇점인지 확인한다.
	#crawling_App_receive_naver_data라는 테이블에서 key1 칼럼이 변수 nowDate 값과 일치하고 N_Word 칼럼이 a와 일치하는 값의 N_Rating를 가져온다.
	#조건절에 nowDate 옵션을 주어서 현재 날짜에 있는 데이터로 범위를 제한한다.
	    sql = "select N_Rating from crawling_App_receive_naver_data where key1=%s and N_Word=%s"
	    curs.execute(sql, (localnowDate, a))
	    num = curs.fetchall()
	    
	#만약 N_Word 값이 존재한다면 
	    if num:
	#DB에서 가져온 데이터의 첫번째 키워드 부터 스무번째 키워드 까지 순서대로 수행
	#기존의 점수 값에서 점수를 더해주는 기능
	        for x in num:
	            d = list(x.values())
	            k = int(d[0])
	            k = k + b
	
	#crawling_App_receive_naver_data라는 테이블에서 N_Word 칼럼이 a와 일치하는 값의 N_Rating을 k변수로 업데이트 한다.
	            sql = "UPDATE crawling_App_receive_naver_data SET N_Rating=%s WHERE N_Word=%s"
	            curs.execute(sql, (k, a))
	            rows = curs.fetchall()
	            conn.commit()
	
	#만약 N_Word 값이 존재하지 않는다면
	    else:
	#crawling_App_receive_naver_data라는 테이블에서 새로운 레코드를 생성한다.(key1 : localnowDate, N_Word : a, N_Rating : b)
	        sql = "INSERT INTO crawling_App_receive_naver_data (key1,N_Word,N_Rating) VALUES(%s,%s,%s)"
	        curs.execute(sql, (localnowDate, a, b))
	        rows = curs.fetchall()
	        conn.commit()
	#키워드 순위가 떨어지면 점수도 1점씩 작게 부여하기 위해서 b에서 1을 뺀다.
	    b = b - 1

	#DB 연결 종료
	conn.close()
	
	
=======
    while(1):
        time.sleep(30)
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')


        html = requests.get('https://www.naver.com/').text
        soup = BeautifulSoup(html, 'html.parser')
        title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
        Machined_title_list = list()
        for idx, title in enumerate(title_list, 1):
            Machined_title_list.append(title.text)

        print(Machined_title_list)
        params = {
            "_date": nowDate,
            "_time": nowTime,
            "_div": 'NAVER',
            "_value": json.dumps(Machined_title_list)
        }

        transaction = CallTransactionBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("transaction_RT") \
            .params(params) \
            .build()
        print(nowDate, nowTime, 'NAVER')
        signed_transaction = SignedTransaction(transaction, wallet)
        tx_hash = icon_service.send_transaction(signed_transaction)
        print(tx_hash)
        time.sleep(10)
        tx_result = icon_service.get_transaction_result(tx_hash)
        print(tx_result['status'])


        #---------------------------------------------GOOGLE----------------------------------------
        now = datetime.datetime.now()
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=800x600')
        options.add_argument("disable-gpu")
        path = "/home/lyu/Downloads/chromedriver"
        driver = webdriver.Chrome(path, chrome_options=options)

        driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all")
        time.sleep(10)

        req = driver.page_source

        soup = BeautifulSoup(req, 'html.parser')

        # time.sleep(10)
        title_list = soup.select('div > span:nth-child(1) > a')


        while not title_list or len(title_list) < 10:
            now = datetime.datetime.now()
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            options.add_argument('window-size=800x600')
            options.add_argument("disable-gpu")
            path = "/home/lyu/Downloads/chromedriver"
            driver = webdriver.Chrome(path, chrome_options=options)

            driver.get("https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all")
            time.sleep(5)
            req = driver.page_source

            soup = BeautifulSoup(req, 'html.parser')
            # time.sleep(10)
            title_list = soup.select('div > span:nth-child(1) > a')
            print(title_list)



        Temp_list = title_list[0:20]
        Machined_Google_title_list = list()

        for title in Temp_list:
            Machined_Google_title_list.append(title.text.strip())


        params_G = {
            "_date": nowDate,
            "_time": nowTime,
            '_div': 'GOOGLE',
            "_value": json.dumps(Machined_Google_title_list)
        }
        transaction_G = CallTransactionBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .step_limit(10_000_000) \
            .nid(3) \
            .nonce(100) \
            .method("transaction_RT") \
            .params(params_G) \
            .build()
        print(nowDate, nowTime, 'GOOGLE')
        signed_transaction_G = SignedTransaction(transaction_G, wallet)
        tx_hash_G = icon_service.send_transaction(signed_transaction_G)
        print(tx_hash_G)
        time.sleep(10)
        tx_result_G = icon_service.get_transaction_result(tx_hash_G)
        print(tx_result_G['status'])

        # ------------------------Google DB Con------------------------

        # MySQL Connection 연결
        conn = pymysql.connect(host='127.0.0.1', user='admin', password='rootroot',
                               db='Crawling_DB', charset='utf8')

        # Connection 으로부터 Cursor 생성
        # curs = conn.cursor()
        curs = conn.cursor(pymysql.cursors.DictCursor)

        b = 20

        # 현재 1등 데이터가 TOP20 테이블에 이미 존재하고 있는지 검사
        check = Machined_Google_title_list[0]
        sql = "select * from crawling_App_receive_google_data where key1=%s and G_Word=%s"
        curs.execute(sql, (nowDate, check))
        check_resuit = curs.fetchall()
        if not check_resuit:
            print("Warning!!!")

        # 가져온 20개의 키워드 insert, update
        for a in Machined_Google_title_list:
            # orgin score call

            # 검색된 단어의 점수가 존재하는 지, 몇점인지 확인한다.
            sql = "select G_Rating from crawling_App_receive_google_data where key1=%s and G_Word=%s"
            curs.execute(sql, (nowDate, a))
            num = curs.fetchall()

            if num:
                # print("already exist")
                for x in num:
                    d = list(x.values())
                    k = int(d[0])
                    k = k + b
                    # 만약 a[0]값이 crawling_receive_google_data에 없으며 주의 메세지 출력

                    sql = "UPDATE crawling_App_receive_google_data SET G_Rating=%s WHERE G_Word=%s"
                    #### 전날 날짜에 업데이트 하게되는 문제
                    curs.execute(sql, (k, a))
                    rows = curs.fetchall()
                    conn.commit()

            else:
                # print("New Input")
                sql = "INSERT INTO crawling_App_receive_google_data (key1,G_Word,G_Rating) VALUES(%s,%s,%s)"
                # sql = "select * from crawling_receive_google_data where key1=%s and G_Word='abc' and G_Rating=%s" % (nowDate, b)
                curs.execute(sql, (nowDate, a, b))
                rows = curs.fetchall()
                conn.commit()

            b = b - 1

        sql = "select G_Word from crawling_App_receive_google_data where key1=%s" % (nowDate)
        curs.execute(sql)
        rows = curs.fetchall()
        print(rows)

        # ------------------------Naver DB Con------------------------

        b=20

        check = Machined_title_list[0]
        sql = "select * from crawling_App_receive_naver_data where key1=%s and N_Word=%s"
        curs.execute(sql, (nowDate, check))
        check_resuit = curs.fetchall()
        if not check_resuit:
            print("Warning!!!")

        # 가져온 20개의 키워드 insert, update
        for a in Machined_title_list:
            # orgin score call

            # 검색된 단어의 점수가 존재하는 지, 몇점인지 확인한다.
            sql = "select N_Rating from crawling_App_receive_naver_data where key1=%s and N_Word=%s"
            curs.execute(sql, (nowDate, a))
            num = curs.fetchall()

            if num:
                # print("already exist")
                for x in num:
                    d = list(x.values())
                    k = int(d[0])
                    k = k + b
                    # 만약 a[0]값이 crawling_receive_google_data에 없으며 주의 메세지 출력

                    sql = "UPDATE crawling_App_receive_naver_data SET N_Rating=%s WHERE N_Word=%s"
                    #### 전날 날짜에 업데이트 하게되는 문제
                    curs.execute(sql, (k, a))
                    rows = curs.fetchall()
                    conn.commit()

            else:

                # print("New Input")
                sql = "INSERT INTO crawling_App_receive_naver_data (key1,N_Word,N_Rating) VALUES(%s,%s,%s)"
                # sql = "select * from crawling_receive_google_data where key1=%s and G_Word='abc' and G_Rating=%s" % (nowDate, b)
                curs.execute(sql, (nowDate, a, b))
                rows = curs.fetchall()
                conn.commit()

            b = b - 1

        sql = "select N_Word from crawling_App_receive_naver_data where key1=%s" % (nowDate)
        curs.execute(sql)
        rows = curs.fetchall()
        print(rows)

        conn.close()

        print("===========================================================================================================================================")
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
