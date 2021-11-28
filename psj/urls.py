from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="homepage"),
    path('search/', views.result,name="searchepage"),
]
