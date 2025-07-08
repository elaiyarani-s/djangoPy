from django.shortcuts import render
from .models import User

# Create your views here

def index(request):
    return render(request,'UserInfo/index.html')

def user(request):
    user = User.objects.all()
    return render(request, 'UserInfo/users.html', {'users': user})
    
