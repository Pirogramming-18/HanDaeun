from django.urls import path 

from posts.views import home, create, detail, update, delete

app_name = "posts"

urlpatterns = [
    path('', home, name="home"),
    path('create', create, name="create"),
    path('post/<int:id>', detail, name="detail"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),
]