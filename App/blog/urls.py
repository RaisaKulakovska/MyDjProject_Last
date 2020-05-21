from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    path('comment', views.comment, name = "comment"),
    path('single', views.single, name = "single")

]