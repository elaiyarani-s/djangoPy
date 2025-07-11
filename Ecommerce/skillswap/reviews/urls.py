from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('add/<str:username>/', views.add_review, name='add'),
]
