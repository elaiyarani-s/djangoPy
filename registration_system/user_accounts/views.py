from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserProfileInfoForm,UserRegistrationForm
from django.utils.timezone import localtime



# Create your views here.

def index(request):
    return render(request,"user_accounts/index.html")

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True    
        else:
            print(user_form.errors,profile_form.errors)
        
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'user_accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered':registered
    })

def account_login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember = request.POST.get('remember', False)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)  

            messages.success(request, 'Successfully logged in.')
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "user_accounts/login.html")


@login_required
def dashboard(request):
    last_login = localtime(request.user.last_login) if request.user.last_login else "First login"
    return render(request, 'user_accounts/dashboard.html', {'last_login': last_login})

@login_required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
def account_logout(request):
    messages.success(request, 'Successfully logged out.')

    logout(request)
    return redirect('index')
    