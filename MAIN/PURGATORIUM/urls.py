from django.urls import path
from .views import home, detail, post, create_post

urlpatterns = [
    path("", home, name="home"),
    path("detail/<slug>/", detail, name="detail"),
    path("post/<slug>/", post, name="post"),
    path("create_post/", create_post, name="create_post"),
]