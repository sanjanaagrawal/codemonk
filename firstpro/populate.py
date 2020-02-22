import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstpro.settings')
import django
django.setup()
import random
from firstapp.models import modeltable
from faker import Faker
fakegen=Faker()

def func(N=5):
    for entry in range(N):
        fake_n=fakegen.name()
        fake_t=fakegen.time()
        fake_dir=fakegen.text()
        fake_des=fakegen.text()
        fake_ing=fakegen.name()
        data=modeltable.objects.get_or_create(name=fake_n,time=fake_t,directions=fake_dir,description=fake_des,ingredients=fake_ing)[0]

if __name__=='__main__':
    func(20)
    print("populating complete")
