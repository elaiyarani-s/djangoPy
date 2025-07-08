from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("<em>My Second App </em>")
    my_dict = {"insert_me":"My Second App rendering templates index.html from views.py"}
    return render(request,"AppTwo/index.html",context=my_dict)

def help(request):
    return render(request, 'AppTwo/help.html')