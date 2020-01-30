import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

# FAKE POP SCRIPTS
import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','MarketPlace','News','Games']

def add_topic():
    t = Topics.objects.get_or_create(topic_name=random.choice(topics))[1]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # Create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = WebPage.objects.get_or_create(topic_name=top,url=fake_url,name=fake_name)[1]

        # Create a fake access record for that WebPage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[1]

if __name__ == '__main__':
    print("populating scripts!")
    populate(20)
    print("populating complete")
