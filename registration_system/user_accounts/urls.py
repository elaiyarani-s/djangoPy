from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name = 'index'),
    path("register/",views.register, name = "register"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.account_logout, name='logout'),
    path("login/", views.account_login, name="login"),


]