from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_carlist, name='carlist'),
    path('<int:carlist_id>', views.singlecar, name='singlecar')
]