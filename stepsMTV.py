# 1. Create the Django Project and App
# 2. Register the app in settings.py (installed_apps)
# 3. Setup templates (templates - dirs/ app_dirs), static and media files (statis_url, static_root & staticfile_dirs, media_root and media_url) in settings.py
# 4. Create models
# 5. Register models in admin.py
# 6. makemigrations. migrate
# 7. Create Modelforms (forms.py)
# 8. Create templates (html - base and then pages extending base.html)
# 9. Create views
# 10. Setup URLs in urls.py
# 11. Create static files (css, images)
# 12. Create faker script (populate_*.py)
# 13. runserver

# ====================================================

# 1. Create the Django Project and App
# django-admin startproject myproject
# cd myproject
# python manage.py startapp mainapp


# 2. Register the App
# In myproject/settings.py, add 'mainapp' to INSTALLED_APPS:
# INSTALLED_APPS = [
#     ...
#     'mainapp',
# ]

# 3. Set Up Templates and Static Files
# a. In settings.py:
# # For Templates (Django already includes this by default)
# TEMPLATES = [
#     {
#         ...
#         'APP_DIRS': True,
#         ...
#     },
# ]

# # For Static files
# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# b. Project folder structure:
# myproject/
# ├── mainapp/
# │   ├── templates/
# │   │   └── mainapp/
# │   │       ├── base.html
# │   │       ├── home.html
# │   │       ├── about.html
# │   │       └── users.html
# │   ├── static/
# │   │   └── mainapp/
# │   │       └── style.css

# 4. Create Models
# In mainapp/models.py:
# from django.db import models

# class User(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
# Then run:
# python manage.py makemigrations
# python manage.py migrate

# 5. Create a Base Template
# mkdir -p templates/mainapp 
# ouch templates/mainapp/index.html
# In mainapp/templates/mainapp/base.html:
# <!DOCTYPE html>
# <html>
# <head>
#     <title>{% block title %}My Site{% endblock %}</title>
#     <link rel="stylesheet" href="{% static 'mainapp/style.css' %}">
# </head>
# <body>
#     <nav>
#         <a href="{% url 'home' %}">Home</a> |
#         <a href="{% url 'about' %}">About</a> |
#         <a href="{% url 'user_list' %}">Users</a>
#     </nav>
#     <hr>
#     <div>
#         {% block content %}{% endblock %}
#     </div>
# </body>
# </html>

# 6. Create Pages Extending base.html
# home.html:
# {% extends "mainapp/base.html" %}
# {% block title %}Home{% endblock %}
# {% block content %}
# <h2>Welcome to the Home Page!</h2>
# {% endblock %}

# 7. Create Views
# In mainapp/views.py:
# from django.shortcuts import render
# from .models import User

# def home(request):
#     return render(request, 'mainapp/home.html')

# def about(request):
#     return render(request, 'mainapp/about.html')

# def user_list(request):
#     users = User.objects.all()
#     return render(request, 'mainapp/users.html', {'users': users})

# 8. Set Up URLs
# touch mainapp/urls.py
# In mainapp/urls.py (create if it doesn't exist):
#                     from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('users/', views.user_list, name='user_list'),
# ]

# In myproject/urls.py:
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('mainapp.urls')),
# ]

# 9. Add Static File Example
# mkdir -p static/css
# touch static/css/styles.css
# In mainapp/static/mainapp/style.css:
# body {
#     font-family: Arial, sans-serif;
#     background-color: #f0f0f8;
#     padding: 20px;
# }
# nav a {
#     margin-right: 10px;
#     text-decoration: none;
# }

# 10. Create Faker Script
# pip install faker
# Create mainapp/populate_users.py:
# import os
# import django
# from faker import Faker

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
# django.setup()

# from mainapp.models import User

# fake = Faker()

# def populate(n=10):
#     for _ in range(n):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = fake.unique.email()
#         User.objects.create(first_name=first_name, last_name=last_name, email=email)

# if __name__ == "__main__":
#     populate(20)
#     print("Populated database with fake users.")

# python mainapp/populate_users.py


# 11. Start the Server
# python manage.py runserver



