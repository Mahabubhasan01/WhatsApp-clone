from unicodedata import name
from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request, 'chat/Home.html')


def Chat_Ui(request):
    return render(request, 'chat/chat_ui.html')
