import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_three.settings')
django.setup()

fakegen = Faker()

from AppThree.models import AccessRecord,Webpage,Topic,UserProfile

topics = ['Search','Social','Marketplace','News','Datascience']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=10):

    for entry in range(N):
        top = add_topic()
    
        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()
    
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
    
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populate complete")


