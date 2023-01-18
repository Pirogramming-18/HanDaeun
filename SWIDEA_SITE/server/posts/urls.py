from django.urls import path
from . import views

app_name = "posts"

urlpatterns= [
    path("", views.posts_list, name="list"),
    path("posts/create", views.posts_create, name="create"),
    path("posts/<int:id>", views.posts_retrieve, name="retrieve"),
    path("posts/<int:id>/update", views.posts_update, name="update"),
    path("posts/<int:id>/delete", views.posts_delete, name="delete"),
    
    path("posts/tool_list", views.tool_list, name="tool_list"),
    path("posts/tool_create", views.tool_create, name="tool_create"),
    path("posts/<int:id>/tool_retrieve", views.tool_retrieve, name="tool_retrieve"),
    path("posts/<int:id>/tool_update", views.tool_update, name="tool_update"),
    path("posts/<int:id>/tool_delete", views.tool_delete, name="tool_delete"),
    
]