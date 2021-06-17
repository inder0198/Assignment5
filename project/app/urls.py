from django.urls import path

from . import views     # it means - 'from all import views'

urlpatterns = [
    path('',views.MainPage.as_view()),
    path('apply',views.mainpage),
    path('output',views.output),
]