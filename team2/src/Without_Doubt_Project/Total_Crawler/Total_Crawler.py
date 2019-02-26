#-----------------------------------------crawling----------------------------------------------
import requests, time, datetime
from bs4 import BeautifulSoup
from selenium import webdriver


#---------------------------------------db connect----------------------------------------------
import pymysql


#---------------------------------------Icon SCORE Service--------------------------------------
import json
from iconsdk.icon_service import IconService
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.builder.transaction_builder import CallTransactionBuilder
from iconsdk.signed_transaction import SignedTransaction
from iconsdk.wallet.wallet import KeyWallet

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


#-------------------------------------------Main source------------------------------------------
class calltransaction_transaction_RT():
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