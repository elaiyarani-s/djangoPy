from django.urls import path
from . import views

urlpatterns = [
    path('skill_list/', views.skill_list, name='skill_list'),
    path('skill_add/', views.skill_add, name='skill_add'),
]
