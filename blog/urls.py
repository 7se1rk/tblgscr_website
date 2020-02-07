from django.urls import path
from . import views


urlpatterns = [
    path('search', views.search, name='search'),
    path('home/', views.home),
    path('login/', views.login, name='login'),
]
