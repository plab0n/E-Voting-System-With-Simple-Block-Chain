from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path('vote_home', views.vote_home, name='vote_home'),

    path('vote/<int:pk>', views.vote, name='vote'),
]