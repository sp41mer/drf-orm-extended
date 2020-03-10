import time

import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from lecture_orm_extended.models import Student


def default():
    query = Student.objects.all()

    for student in query:
        a = student.name

    for student in query:
        a = student.name

    for student in query:
        a = student.name

    for student in query:
        a = student.name


def with_iterator():
    print('Iterator')
    time.sleep(1)
    query = Student.objects.all()

    for student in query.iterator():
        a = student.name

    for student in query.iterator():
        a = student.name

    for student in query.iterator():
        a = student.name

    for student in query.iterator():
        a = student.name


default()
time.sleep(3)
with_iterator()
