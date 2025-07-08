from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length=264,unique=True)

    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self) :
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)
    
class UserProfile(models.Model):
    webpage = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField()
    comment = models.TextField(blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.username} | {self.webpage}"