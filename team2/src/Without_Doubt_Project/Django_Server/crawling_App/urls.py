from django.conf.urls import url
#from django.urls import path, include
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.input),
    url(r'^realtime.html$', views.index),
    url(r'^realtime_google.html$', views.index2),
    url(r'^realtime_Top20.html$', views.top),
    url(r'^realtime_Top20_google.html$', views.top2),
    
    #url(r'^(?P<id>.*)/$', views.input, name='input'),
    #path('<word>/',views.input),
    #path('',views.index),    
]