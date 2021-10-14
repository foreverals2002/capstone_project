from django.contrib import admin
from django.urls import path, include
from my_api import views


urlpatterns = [
    path('hello/', views.hello),
    path(r'morning/<int:test>/', views.morning),
    path('testjson/', views.TestJson.as_view()),
]
