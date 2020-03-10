import time

import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from lecture_orm_extended.models import Student, City, School


def dummy_update():
    for student in Student.objects.filter(number_of_articles=3):
        student.number_of_articles = 4
        student.save()


def bulk_update():
    print("STARTED")
    time.sleep(1)
    Student.objects.filter(number_of_articles=4).update(number_of_articles=5)


dummy_update()
time.sleep(3)
bulk_update()
