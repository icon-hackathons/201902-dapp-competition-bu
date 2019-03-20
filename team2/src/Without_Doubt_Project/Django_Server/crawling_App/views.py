#-------------------------------------ICON_SCORE-------------------------------------------
import json, time, datetime
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService
from iconsdk.builder.call_builder import CallBuilder

<<<<<<< HEAD
#-------------------------------------Server-------------------------------------------
# 데이터베이스 테이블 모델 추가
from .models import Receive_Google_Data, Receive_Naver_Data, Missing_Data
#클라이언트의 요청에 결과값을 보내주기 위해 render 라이브러리 추가
from django.shortcuts import render
#웹페이지에 에러 메세지를 출력해주기 위해 HttpResponse 라이브러리 추가
from django.http import HttpResponse
#Local 타임존을 UTC 타임존으로 변환하기 위한 라이브러리 추가
from datetime import timedelta

#-------------------------------------ICON_SCORE_option-------------------------------------------
_score_address = "cxb7ef03fea5fa9b2fe1f00f548d6da7ff2ddfebd5"
_keystore_address = "hx226e6e4340136836b36977bd76ca83746b8b071c"
node_uri = "https://ctz.solidwallet.io/api/v3"
=======

#-------------------------------------Server-------------------------------------------
from .models import Receive_Google_Data, Receive_Naver_Data
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
#from django_pandas.io import read_frame
#from django_pandas.managers import DataFrameManager
#from IPython.display import display


#-------------------------------------ICON_SCORE_option-------------------------------------------
_score_address = "cxd8477e0e67273112e64ed81ab5b578bb4f997da6"
_keystore_address = "hx055ca4808e82f7c0e4eafa884cefcfec15e8387b"
node_uri = "http://localhost:9000/api/v3"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
icon_service = IconService(HTTPProvider(node_uri))


#-------------------------------------Naver RT-------------------------------------------
<<<<<<< HEAD
#네이버 실시간 검색어 기능 구현

#index라는 메소드를 선언
def index(request):

#realtime.html에서 get방식을 통해 입력된 값을 불러오는 부분
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")


#가져온 데이터를 스코어 파라미터에 맞는 형태로 수정하는 작업
#날짜와 시간 데이터 입력이 있는경우
    if userdate and usertime :
#날짜 데이터 XXXX-XX-XX형태를 XXXXXXXX폼으로 수정
        split_Date = userdate.split('-')
        split_Time = usertime.split(':') 
#시간 데이터 XX:XX형태를 XXXX폼으로 수정
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

#5분단위로 검색할수 있게 하기위해서 5를 나눈 나머지가 0이 아닌때 오류 메세지 출력
        if int(input_Time) % 5 != 0:
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime.html', {'error' : error})

#2019-02-00~2020-02-00으로 날짜 범위를 정해준다. 
#아래 날짜를 수정하여 원하는 범위를 지정해줄 수 있다.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#로컬 타임존을 utc타임존으로 수정하는 부분
#구한 날짜와 시간을 합쳐 datatime형식으로 만들고 9시간만큼 뺀 시간을 구한다.
            now = userdate + " " + usertime + ":00"
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  
            now = now - timedelta(hours=9)

#수정된 시간대에서 날짜와 시간을 추출한다.
            nowDate = now.strftime('%Y%m%d')
            nowTime = now.strftime('%H%M')
          
            params = {
                "_Call_date": nowDate,
                "_Call_time": nowTime,
=======

def index(request):
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

    if userdate and usertime :
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

            params = {
                "_Call_date": "".join(input_Date),
                "_Call_time": "".join(input_Time),
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
                "_Call_div": "NAVER"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()
<<<<<<< HEAD
            response = icon_service.call(Inquiry)

#만약 데이터가 스코어에 존재하지 않는 경우
            if response == "":
                
                error = 1
#urls.py에 의해 들어온 사용자의 요청에 realtime.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
                return render(request, 'crawling/realtime.html', {'error' : error})
#만약 데이터가 스코어에 존재하는 경우
            else:
#가져온 데이터를 posts라는 변수에 담는다.
                posts = json.loads(response)
#Missing_Data 테이블에서 누락값을 가져와 missing이라는 변수에 담는다.
                missing = Missing_Data.objects.filter(key1=input_Date ,Type="N")
#urls.py에 의해 들어온 사용자의 요청에 realtime.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 날짜 값이 담긴 date, 시간 값이 담긴 time 변수, 누락값이 담긴 missing변수와 함께 보내준다.
                return render(request, 'crawling/realtime.html', {'posts': posts, 'date': userdate, 'time': usertime, 'missing':missing})

#만약 2019-02-00~2020-02-00의 범위를 초과하였을 경우
        else: 
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime.html', {'error' : error})

#날짜와 시간 데이터 입력이 없는 경우
    elif userdate == None or usertime == None:
#utc타임존 시간과 로컬 타임존 시간을 구한다.
        now = datetime.datetime.utcnow()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')

        localnow = datetime.datetime.now()
        localnowDate = localnow.strftime('%Y%m%d')
        localnowTime = localnow.strftime('%H%M')


#현재시간을 5의 배수로 만들어 준다.
#현재시간이 5의 배수면 아직 데이터가 업데이트 되지 않을 경우를 방지해 현재시간 5분전에 데이터를 구한다.
#현재시간이 5의 배수가 아닌 경우 5로 나눈 나머지 만큼 빼준다.

        if int(nowTime) % 100 == 0 :
            realTime = int(nowTime) - 45
        elif int(nowTime) % 5 == 0 :
            realTime = int(nowTime) - 5
        elif int(nowTime) % 5 == 1 :
            realTime = int(nowTime) - 1
        elif int(nowTime) % 5 == 2 :
            realTime = int(nowTime) - 2
        elif int(nowTime) % 5 == 3 :
            realTime = int(nowTime) - 3
        elif int(nowTime) % 5 == 4 :
            realTime = int(nowTime) - 4

# *** UTC시간 0000분이면 -5가 저장되어버림
#만약 구글 크롤링 오버헤드에 의해 26분에 값이 저장했을 경우 테이블을 하나더 만들어 예외처리 할 수 있다.
         

#00시09분 이하의 경우에는 정수형으로 치환할 경우 한자리로 변경되어버리기 때문에 000을 추가한다.
        if realTime <= 9:
            realTime = "000" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 800으로 변경되어버리기 때문에 00을 추가한다.
        elif realTime <= 59 and realTime >= 10:
            realTime = "00" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 세자리로 변경되어버리기 때문에 0을 추가한다.
        elif realTime <= 959 and realTime >= 60:
            realTime = "0" + str(realTime)

        params = {
            "_Call_date": nowDate,
            "_Call_time": realTime,
            "_Call_div": "NAVER"

#테스트용 날짜, 시간값 (데이터가 담겨있다.)
            #"_Call_date": "20190308",
            #"_Call_time": "0723",
=======

            response = icon_service.call(Inquiry)
            posts = json.loads(response)
            return render(request, 'crawling/realtime.html', {'posts': posts})
        else:
            posts = str(Receive_Naver_Data.objects.last())
            # return render(request, 'crawling/realtime, {'posts' : posts})
            return HttpResponse("No data aaa" + userdate)


    elif userdate == None or usertime == None:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')
        # return HttpResponse("No data aaa" + nowDate + nowTime)
        realTime = int(nowTime) - 1
        shit = str(realTime)
        params = {
            "_Call_date": nowDate,
            "_Call_time": shit,
            "_Call_div": "NAVER"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
<<<<<<< HEAD

#현재시간을 5의 배수로 만들어 준다.
#현재시간이 5의 배수면 아직 데이터가 업데이트 되지 않을 경우를 방지해 현재시간 5분전에 데이터를 구한다.
#현재시간이 5의 배수가 아닌 경우 5로 나눈 나머지 만큼 빼준다.

        if int(localnowTime) % 100 == 0 :
            realTime = int(nowTime) - 45
        elif int(localnowTime) % 5 == 0 :
            localrealTime = int(localnowTime) - 5
        elif int(localnowTime) % 5 == 1 :
            localrealTime = int(localnowTime) - 1
        elif int(localnowTime) % 5 == 2 :
            localrealTime = int(localnowTime) - 2
        elif int(localnowTime) % 5 == 3 :
            localrealTime = int(localnowTime) - 3
        elif int(localnowTime) % 5 == 4 :
            localrealTime = int(localnowTime) - 4

#만약 구글 크롤링 오버헤드에 의해 26분에 값이 저장했을 경우 테이블을 하나더 만들어 예외처리 할 수 있다.
         

#00시09분 이하의 경우에는 정수형으로 치환할 경우 한자리로 변경되어버리기 때문에 000을 추가한다.
        if localrealTime <= 9:
            localrealTime = "000" + str(localrealTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 800으로 변경되어버리기 때문에 00을 추가한다.
        elif localrealTime <= 59 and localrealTime >= 10:
            localrealTime = "00" + str(localrealTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 세자리로 변경되어버리기 때문에 0을 추가한다.
        elif localrealTime <= 959 and localrealTime >= 60:
            localrealTime = "0" + str(localrealTime)

#UTC시간으로 15:00을 넘으면 날짜에서 하루를 추가한다.            
#        if realTime >= 1500:
#           nowDate = int(nowDate) + 1
#UTC타임존을 asia/seoul타임존으로 변경하기 위해 9시간을 추가해준다.
#        realTime = (int(realTime) + 900) % 2400
#00시09분 이하의 경우에는 정수형으로 치환할 경우 한자리로 변경되어버리기 때문에 000을 추가한다.
#        if realTime <= 9:
#            realTime = "000" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 800으로 변경되어버리기 때문에 00을 추가한다.
#        elif realTime <= 59 and realTime >= 10:
#            realTime = "00" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 세자리로 변경되어버리기 때문에 0을 추가한다.
#        elif realTime <= 959 and realTime >= 60:
#            realTime = "0" + str(realTime)


#만약 스코어의 최근시간에 값이 존재하지 않을 경우
        if response == "":
#웹화면에 검색된 날짜,시간과 함께 최근 값이 존재하지 않다는 메세지를 출력해준다.
            return HttpResponse("Recent Data (" + str(localnowDate) + " " + str(localrealTime) + ") is Empty")

        posts = json.loads(response)

#datetime함수로 가져온 날짜와 시간정보를 웹페이지에 출력해 주기위해 알맞는 데이터 폼으로 수정한다.
#XXXX XX XX의 첫번째 자리 부터 네번째 자리를 temp1변수에 담는다.
        temp1 = str(localnowDate)[0:4]
#XXXX XX XX의 다섯번째 자리 부터 여섯번째 자리를 temp2변수에 담는다.
        temp2 = str(localnowDate)[4:6]
#XXXX XX XX의 일곱번째자리 부터 여덞번째 자리를 temp3변수에 담는다.
        temp3 = str(localnowDate)[6:8]
#위 세개의 변수를 취합해 XXXX-XX-XX형태로 만든다
        convert_date = temp1 + "-" + temp2 + "-" + temp3

#XXXX의 첫번째 자리부터 두번째 자리를 temp1변수에 담는다
        temp1 = str(localrealTime)[0:2]
#XXXX의 세번째 자리부터 네번째 자리를 temp2변수에 담는다
        temp2 = str(localrealTime)[2:4]
#위 두개의 변수를 취합해 XX:XX형태로 만든다.
        convert_time = temp1 + ":" + temp2

        missing = Missing_Data.objects.filter(key1=localnowDate,Type="N")

#urls.py에 의해 들어온 사용자의 요청에 realtime.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 알맞은 형태로 만든 날짜, 시간 변수, 누락값 변수와 함께 보내준다.
        return render(request, 'crawling/realtime.html', {'posts' : posts, 'date': convert_date,'time':convert_time,'missing':missing})


#-------------------------------------Google RT-------------------------------------------
#구글 실시간 검색어 기능 구현

#index2라는 메소드를 선언
def index2(request):

#realtime_google.html에서 get방식을 통해 입력된 값을 불러오는 부분
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

#가져온 데이터를 스코어 파라미터에 맞는 형태로 수정하는 작업
#날짜와 시간 데이터 입력이 있는경우
    if userdate and usertime :
#날짜 데이터 XXXX-XX-XX형태를 XXXXXXXX폼으로 수정
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
#시간 데이터 XX:XX형태를 XXXX폼으로 수정
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

#5분단위로 검색할수 있게 하기위해서 5를 나눈 나머지가 0이 아닌때 오류 메세지 출력
        if int(input_Time) % 5 != 0:
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime_google.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime_google.html', {'error' : error})

#2019-02-00~2020-02-00으로 날짜 범위를 정해준다. 
#아래 날짜를 수정하여 원하는 범위를 지정해줄 수 있다.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:
            
#로컬 타임존을 utc타임존으로 수정하는 부분
#구한 날짜와 시간을 합쳐 datatime형식으로 만들고 9시간만큼 뺀 시간을 구한다.
            now = userdate + " " + usertime + ":00"
            now = datetime.datetime.strptime(now, '%Y-%m-%d %H:%M:%S')  
            now = now - timedelta(hours=9)

#수정된 시간대에서 날짜와 시간을 추출한다.
            nowDate = now.strftime('%Y%m%d')
            nowTime = now.strftime('%H%M')

            params = {
                "_Call_date": nowDate,
                "_Call_time": nowTime,
=======
        posts = json.loads(response)
        # userdate = Receive_Naver_Data.objects.last().date - recent DB data call
        # posts = list(Post.objects.filter(date=userdate))
        return render(request, 'crawling/realtime.html', {'posts': posts})


#-------------------------------------Google RT-------------------------------------------

def index2(request):
    userdate = request.GET.get("userdate")
    usertime = request.GET.get("usertime")

    if userdate and usertime :
        split_Date = userdate.split('-')
        split_Time = usertime.split(':')
        input_Date = "".join(split_Date)
        input_Time = "".join(split_Time)

        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

            params = {
                "_Call_date": "".join(input_Date),
                "_Call_time": "".join(input_Time),
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
                "_Call_div": "GOOGLE"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()
<<<<<<< HEAD
            response = icon_service.call(Inquiry)

#만약 데이터가 스코어에 존재하지 않는 경우
            if response == "":
                error = 1
#urls.py에 의해 들어온 사용자의 요청에 realtime_google.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
                return render(request, 'crawling/realtime_google.html', {'error' : error})
#만약 데이터가 스코어에 존재하는 경우
            else:
#가져온 데이터를 posts라는 변수에 담는다.
                posts = json.loads(response)
#Missing_Data 테이블에서 누락값을 가져와 missing이라는 변수에 담는다.
                missing = Missing_Data.objects.filter(key1=input_Date ,Type="N")
#urls.py에 의해 들어온 사용자의 요청에 realtime_google.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 날짜 값이 담긴 date, 시간 값이 담긴 time 변수, 누락값이 담긴 missing변수와 함께 보내준다.
                return render(request, 'crawling/realtime_google.html', {'posts': posts, 'date': userdate, 'time': usertime,'missing':missing})

#만약 2019-02-00~2020-02-00의 범위를 초과하였을 경우
        else: 
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime_google.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime_google.html', {'error' : error})

#날짜와 시간 데이터 입력이 없는 경우
    elif userdate == None or usertime == None:
#utc타임존 시간과 로컬 타임존 시간을 구한다.
        now = datetime.datetime.utcnow()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')

        localnow = datetime.datetime.now()
        localnowDate = localnow.strftime('%Y%m%d')
        localnowTime = localnow.strftime('%H%M')

#현재시간을 5의 배수로 만들어 준다.
#현재시간이 5의 배수면 아직 데이터가 업데이트 되지 않을 경우를 방지해 현재시간 5분전에 데이터를 구한다.
#현재시간이 5의 배수가 아닌 경우 5로 나눈 나머지 만큼 빼준다.

        if int(nowTime) % 100 == 0 :
            realTime = int(nowTime) - 45        
        elif int(nowTime) % 5 == 0 :
            realTime = int(nowTime) - 5
        elif int(nowTime) % 5 == 1 :
            realTime = int(nowTime) - 1
        elif int(nowTime) % 5 == 2 :
            realTime = int(nowTime) - 2
        elif int(nowTime) % 5 == 3 :
            realTime = int(nowTime) - 3
        elif int(nowTime) % 5 == 4 :
            realTime = int(nowTime) - 4

#00시09분 이하의 경우에는 정수형으로 치환할 경우 한자리로 변경되어버리기 때문에 000을 추가한다.
        if realTime <= 9:
            realTime = "000" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 800으로 변경되어버리기 때문에 00을 추가한다.
        elif realTime <= 59 and realTime >= 10:
            realTime = "00" + str(realTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 세자리로 변경되어버리기 때문에 0을 추가한다.
        elif realTime <= 959 and realTime >= 60:
            realTime = "0" + str(realTime)

        params = {
            "_Call_date": nowDate,
            "_Call_time": realTime,
            "_Call_div": "GOOGLE"

#테스트용 날짜, 시간값 (데이터가 담겨있다.)
            #"_Call_date": "20190227",
            #"_Call_time": "0853",
=======

            response = icon_service.call(Inquiry)
            posts = json.loads(response)
            return render(request, 'crawling/realtime_google.html', {'posts': posts})
        else:
            posts = str(Receive_Google_Data.objects.last())
            # return render(request, 'crawling/realtime, {'posts' : posts})
            return HttpResponse("No data aaa" + userdate)


    elif userdate == None or usertime == None:
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y%m%d')
        nowTime = now.strftime('%H%M')
        # return HttpResponse("No data aaa" + nowDate + nowTime)
        realTime = int(nowTime) - 1
        shit = str(realTime)
        params = {
            "_Call_date": nowDate,
            "_Call_time": shit,
            "_Call_div": "GOOGLE"
>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
<<<<<<< HEAD

#현재시간을 5의 배수로 만들어 준다.
#현재시간이 5의 배수면 아직 데이터가 업데이트 되지 않을 경우를 방지해 현재시간 5분전에 데이터를 구한다.
#현재시간이 5의 배수가 아닌 경우 5로 나눈 나머지 만큼 빼준다.
        if int(localnowTime) % 100 == 0 :
            realTime = int(nowTime) - 45    
        elif int(localnowTime) % 5 == 0 :
            localrealTime = int(localnowTime) - 5
        elif int(localnowTime) % 5 == 1 :
            localrealTime = int(localnowTime) - 1
        elif int(localnowTime) % 5 == 2 :
            localrealTime = int(localnowTime) - 2
        elif int(localnowTime) % 5 == 3 :
            localrealTime = int(localnowTime) - 3
        elif int(localnowTime) % 5 == 4 :
            localrealTime = int(localnowTime) - 4

#만약 구글 크롤링 오버헤드에 의해 26분에 값이 저장했을 경우 테이블을 하나더 만들어 예외처리 할 수 있다.
         
#00시09분 이하의 경우에는 정수형으로 치환할 경우 한자리로 변경되어버리기 때문에 000을 추가한다.
        if localrealTime <= 9:
            localrealTime = "000" + str(localrealTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 800으로 변경되어버리기 때문에 00을 추가한다.
        elif localrealTime <= 59 and localrealTime >= 10:
            localrealTime = "00" + str(localrealTime)
#09시59분 이하의 경우에는 정수형으로 치환할 경우 세자리로 변경되어버리기 때문에 0을 추가한다.
        elif localrealTime <= 959 and localrealTime >= 60:
            localrealTime = "0" + str(localrealTime)


#만약 스코어의 최근시간에 값이 존재하지 않을 경우
        if response == "":
#웹화면에 검색된 날짜,시간과 함께 최근 값이 존재하지 않다는 메세지를 출력해준다.
            return HttpResponse("Recent Data (" + str(nowDate) + " " + str(realTime) + ") is Empty")

        posts = json.loads(response)

#datetime함수로 가져온 날짜와 시간정보를 웹페이지에 출력해 주기위해 알맞는 데이터 폼으로 수정한다.
#XXXX XX XX의 첫번째 자리 부터 네번째 자리를 temp1변수에 담는다.
        temp1 = str(localnowDate)[0:4]
#XXXX XX XX의 다섯번째 자리 부터 여섯번째 자리를 temp2변수에 담는다.
        temp2 = str(localnowDate)[4:6]
#XXXX XX XX의 일곱번째자리 부터 여덞번째 자리를 temp3변수에 담는다.
        temp3 = str(localnowDate)[6:8]
#위 세개의 변수를 취합해 XXXX-XX-XX형태로 만든다
        convert_date = temp1 + "-" + temp2 + "-" + temp3

#XXXX의 첫번째 자리부터 두번째 자리를 temp1변수에 담는다
        temp1 = str(localrealTime)[0:2]
#XXXX의 세번째 자리부터 네번째 자리를 temp2변수에 담는다
        temp2 = str(localrealTime)[2:4]
#위 두개의 변수를 취합해 XX:XX형태로 만든다.
        convert_time = temp1 + ":" + temp2

        missing = Missing_Data.objects.filter(key1=localnowDate,Type="G")

#urls.py에 의해 들어온 사용자의 요청에 realtime_google.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 알맞은 형태로 만든 날짜, 시간 변수, 누락값 변수와 함께 보내준다.
        return render(request, 'crawling/realtime_google.html', {'posts' : posts, 'date': convert_date,'time':convert_time,'missing':missing})


#-------------------------------------Naver Top20-------------------------------------------
#네이버 일일 TOP20 기능 구현

#top 이라는 메소드 생성
def top(request):

#realtime_Top20.html에서 get방식을 통해 입력된 값을 불러오는 부분
    userdate = request.GET.get("userdate")

#가져온 데이터를 스코어 파라미터에 맞는 형태로 수정하는 작업
#데이터 입력이 있는경우
    if userdate:
#날짜 데이터 XXXX-XX-XX형태를 XXXXXXXX폼으로 수정
        split_Date = userdate.split('-')
        input_Date = "".join(split_Date)

#2019-02-00~2020-02-00으로 날짜 범위를 정해준다. 
#아래 날짜를 수정하여 원하는 범위를 지정해줄 수 있다.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#Receive_Naver_Data라는 테이블에서 key1컬럼이 input_Date변수와 일치하는 값을 N_Rating순으로 정렬하여 temp_posts변수에 담는다.
            temp_posts = list(Receive_Naver_Data.objects.filter(key1=input_Date).order_by('-N_Rating'))
#가져온 데이터를 20개로 제한한다.
            posts = temp_posts[0:20]
#만약 데이터가 존재하지 않을 경우
            if len(posts) <= 1 :
                error = 1
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
                return render(request, 'crawling/realtime_Top20.html', {'error' : error})
#만약 데이터가 존재하는 경우
            else :
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 날짜 값이 담긴 userdate 변수와 함께 보내준다.
                return render(request, 'crawling/realtime_Top20.html', {'posts': posts, 'date': userdate})

#만약 2019-02-00~2020-02-00의범위를 초과하였을 경우
        else:
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime_Top20.html', {'error' : error})

#데이터 입력이 없는 경우
#가장 최근데이터를 출력해주기 위한 기능
    else:
#Receive_Naver_Data 테이블에 아무 값도 저장되어 있지 않은지 확인한다.
        check = Receive_Naver_Data.objects.all()

#만약 값이 존재한다면.
        if check :
#Receive_Naver_Data라는 테이블에서 가장 최근에 저장된 값의 key1컬럼을 가지고와 userdate에 담는다
            userdate = Receive_Naver_Data.objects.last().key1

#테이블에서 가져온 널쩌정보를 웹페이지에 출력해 주기위해 알맞는 데이터 폼으로 수정한다.
#XXXX XX XX의 첫번째 자리 부터 네번째 자리를 temp1변수에 담는다.
            temp1 = str(userdate)[0:4]
#XXXX XX XX의 다섯번째 자리 부터 여섯번째 자리를 temp2변수에 담는다.
            temp2 = str(userdate)[4:6]
#XXXX XX XX의 일곱번째자리 부터 여덞번째 자리를 temp3변수에 담는다.
            temp3 = str(userdate)[6:8]
#위 세개의 변수를 취합해 XXXX-XX-XX형태로 만든다
            convert_date = temp1 + "-" + temp2 + "-" + temp3

#Receive_Naver_Data라는 테이블에서 key1컬럼이 userdate변수와 일치하는 값을 N_Rating순으로 정렬하여 temp_posts변수에 담는다.
            temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
#가져온 데이터를 20개로 제한한다.
            posts = temp_posts[0:20]
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 변경한 날짜데이터인 convert_date변수와 함께 보내준다.
            return render(request, 'crawling/realtime_Top20.html', {'posts': posts,'date':convert_date})
#만약 테이블에 아무 값도 저장되어 있지 않다면
        else :
#웹페이지에 아무 데이터가 없다는 메세지 출력
            return HttpResponse("DB is Empty")

#-------------------------------------Google Top20-------------------------------------------
#구글 일일 TOP20 기능 구현

#top 이라는 메소드 생성
def top2(request):
    
#realtime_Top20_google.html에서 get방식을 통해 입력된 값을 불러오는 부분
    userdate = request.GET.get("userdate")

#가져온 데이터를 스코어 파라미터에 맞는 형태로 수정하는 작업
#데이터 입력이 있는경우
    if userdate:
#날짜 데이터 XXXX-XX-XX형태를 XXXXXXXX폼으로 수정
        split_Date = userdate.split('-')
        input_Date = "".join(split_Date)

#2019-02-00~2020-02-00으로 날짜 범위를 정해준다. 
#아래 날짜를 수정하여 원하는 범위를 지정해줄 수 있다.
        if int(input_Date) >= 20190200 and int(input_Date) <= 20200200:

#Receive_Google_Data라는 테이블에서 key1컬럼이 input_Date변수와 일치하는 값을 G_Rating순으로 정렬하여 temp_posts변수에 담는다.
            temp_posts = list(Receive_Google_Data.objects.filter(key1=input_Date).order_by('-G_Rating'))
#가져온 데이터를 20개로 제한한다.
            posts = temp_posts[0:20]
#만약 데이터가 존재하지 않을 경우
            if len(posts) <= 1 :
                error = 1
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20_google.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
                return render(request, 'crawling/realtime_Top20_google.html', {'error' : error})
#만약 데이터가 존재하는 경우
            else :
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20_google.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 날짜 값이 담긴 userdate 변수와 함께 보내준다.
                return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts, 'date': userdate})

#만약 2019-02-00~2020-02-00의범위를 초과하였을 경우
        else:
            error = 2
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20_google.html템플릿과 에러를 알리는 error 파라메터를 보낸다.
            return render(request, 'crawling/realtime_Top20_google.html', {'error' : error})

#데이터 입력이 없는 경우
#가장 최근데이터를 출력해주기 위한 기능
    else:
#Receive_Google_Data 테이블에 아무 값도 저장되어 있지 않은지 확인한다.
        check = Receive_Google_Data.objects.all()

#만약 값이 존재한다면.
        if check :
#Receive_Google_Data라는 테이블에서 가장 최근에 저장된 값의 key1컬럼을 가지고와 userdate에 담는다
            userdate = Receive_Google_Data.objects.last().key1

#테이블에서 가져온 널쩌정보를 웹페이지에 출력해 주기위해 알맞는 데이터 폼으로 수정한다.
#XXXX XX XX의 첫번째 자리 부터 네번째 자리를 temp1변수에 담는다.
            temp1 = str(userdate)[0:4]
#XXXX XX XX의 다섯번째 자리 부터 여섯번째 자리를 temp2변수에 담는다.
            temp2 = str(userdate)[4:6]
#XXXX XX XX의 일곱번째자리 부터 여덞번째 자리를 temp3변수에 담는다.
            temp3 = str(userdate)[6:8]
#위 세개의 변수를 취합해 XXXX-XX-XX형태로 만든다
            convert_date = temp1 + "-" + temp2 + "-" + temp3

#Receive_Google_Data라는 테이블에서 key1컬럼이 userdate변수와 일치하는 값을 G_Rating순으로 정렬하여 temp_posts변수에 담는다.
            temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
#가져온 데이터를 20개로 제한한다.
            posts = temp_posts[0:20]
#urls.py에 의해 들어온 사용자의 요청에 realtime_Top20_google.html템플릿을 실시간 검색 순위가 담긴 posts 변수와 변경한 날짜데이터인 convert_date변수와 함께 보내준다.
            return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts,'date':convert_date})
#만약 테이블에 아무 값도 저장되어 있지 않다면
        else :
#웹페이지에 아무 데이터가 없다는 메세지 출력
            return HttpResponse("DB is Empty")

#-------------------------------------Main Template-------------------------------------------

#urls.py에 의해 들어온 사용자의 요청에 index.html 템플릿을 보내준다.
=======
        posts = json.loads(response)
        # userdate = Receive_Naver_Data.objects.last().date - recent DB data call
        # posts = list(Post.objects.filter(date=userdate))
        return render(request, 'crawling/realtime_google.html', {'posts': posts})


def top(request):
    userdate = request.GET.get("userdate")
    if userdate == None:
        userdate = Receive_Naver_Data.objects.last().key1
        temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
        posts = temp_posts[0:20]

    elif int(userdate) >= 20190200 and int(userdate) <= 20200200:
        temp_posts = list(Receive_Naver_Data.objects.filter(key1=userdate).order_by('-N_Rating'))
        posts = temp_posts[0:20]

    else:
        return render(request, 'crawling/realtime_Top20.html')

    return render(request, 'crawling/realtime_Top20.html', {'posts': posts})


def top2(request):

    userdate = request.GET.get("userdate")
    if userdate == None:
        userdate = Receive_Google_Data.objects.last().key1
        temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
        posts = temp_posts[0:20]

    elif int(userdate) >= 20190200 and int(userdate) <= 20200200:
        temp_posts = list(Receive_Google_Data.objects.filter(key1=userdate).order_by('-G_Rating'))
        posts = temp_posts[0:20]

    else:
        return render(request, 'crawling/realtime_Top20_google.html')

    return render(request, 'crawling/realtime_Top20_google.html', {'posts': posts})


>>>>>>> 86dc0cf045a62ff479b3219fa666841a66152774
def input(request):
    return render(request, 'crawling/index.html')



