from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home/', views.home),
    path('login/', views.login, name='login'),
]
