#url 명령을 사용하기 위해 conf.urls 라이브러리에서 url을 불러온다.
from django.conf.urls import url
from . import views

urlpatterns = [
#기본주소 127.0.0.1:8000/ 으로 url 요청이 있을 경우에 views.py 파일의 input 함수를 사용한다.
    url(r'^$', views.input),				
#127.0.0.1:8000/realtime.html/ 으로 url 요청이 있을 경우에 views.py 파일의 index 함수를 사용한다.
    url(r'^realtime.html$', views.index),
#127.0.0.1:8000/realtime_google.html/ 으로 url 요청이 있을 경우에 views.py 파일의 index2 함수를 사용한다.
    url(r'^realtime_google.html$', views.index2),
#127.0.0.1:8000/realtime_Top20.html/ 으로 url 요청이 있을 경우에 views.py 파일의 top 함수를 사용한다.
    url(r'^realtime_Top20.html$', views.top),
#127.0.0.1:8000/realtime_Top20_google.html/ 으로 url 요청이 있을 경우에 views.py 파일의 top2 함수를 사용한다.
    url(r'^realtime_Top20_google.html$', views.top2),
]