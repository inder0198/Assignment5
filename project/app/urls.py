from django.conf.urls import url
from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.MainPage.as_view()),
    path('apply',views.mainpage),
    path('output',views.output),
    url(r'^down_file', views.down_file),
]