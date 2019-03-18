from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

#기본 주소로 요청이 들어오면 crawling_App이라는 앱의 ulrs에 전송해 추가 명령을 찾게 한다.
    url(r'', include('crawling_App.urls')),
    ]