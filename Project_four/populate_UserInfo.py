import os
import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_four.settings')
django.setup()

from UserInfo.models import User
fake = Faker()


def populate(N=10): 

    for entry in range(N):

        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        
        User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email)
    

if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populate complete")


