from tkinter import N
from . import views
from django.urls import path
urlpatterns = [
    path('', views.Home, name='home'),
    path('chat/', views.Chat_Ui, name='chat'),
]
