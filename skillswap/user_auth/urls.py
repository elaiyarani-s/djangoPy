from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name = 'index'),
    path('register/',views.user_signup, name = 'register'),
    path('login/', views.User_login, name='login'),
    path('logout/', views.User_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),

]