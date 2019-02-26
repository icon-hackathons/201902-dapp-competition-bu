from django.conf.urls import include, url
from django.contrib import admin
# from django.urls import path, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('crawling_App.urls')),
    ]