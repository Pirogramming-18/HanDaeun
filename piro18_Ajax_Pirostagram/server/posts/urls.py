from django.urls import path 

from . import views

app_name = "posts"

urlpatterns = [
    path('', views.home, name="home"),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
]