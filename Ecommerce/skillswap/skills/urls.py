from django.urls import path
from . import views

app_name = 'skills'

urlpatterns = [
    path('', views.skill_list, name='list'),
    path('<int:pk>/', views.skill_detail, name='detail'),
    path('create/', views.skill_create, name='create'),
    # other paths...
]
