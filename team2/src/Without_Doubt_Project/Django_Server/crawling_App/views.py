#-------------------------------------ICON_SCORE-------------------------------------------
import json, time, datetime
from iconsdk.providers.http_provider import HTTPProvider
from iconsdk.icon_service import IconService
from iconsdk.builder.call_builder import CallBuilder


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
icon_service = IconService(HTTPProvider(node_uri))


#-------------------------------------Naver RT-------------------------------------------

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
                "_Call_div": "NAVER"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()

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
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
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
                "_Call_div": "GOOGLE"
            }

            Inquiry = CallBuilder() \
                .from_(_keystore_address) \
                .to(_score_address) \
                .method("inquiry_RT") \
                .params(params) \
                .build()

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
        }

        Inquiry = CallBuilder() \
            .from_(_keystore_address) \
            .to(_score_address) \
            .method("inquiry_RT") \
            .params(params) \
            .build()

        response = icon_service.call(Inquiry)
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


def input(request):
    return render(request, 'crawling/index.html')



