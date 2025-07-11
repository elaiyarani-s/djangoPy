from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Skill(models.Model):

    TYPE_CHOICE = [('offer', 'Offer'), ('request', 'Request')]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    availability = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    skill_type = models.CharField(choices=TYPE_CHOICE, max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
