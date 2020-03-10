import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from lecture_orm_extended.models import Student, City, School
from random import randrange


def populate_db():

    cities = [City.objects.create(name="City {}".format(i * 42), population=randrange(100000, 200000)) for i in range(0,10)]
    schools = [School.objects.create(name="School of {}".format(city.name), number=randrange(9999), city=city) for i in range(0,10) for city in cities]
    student = [Student.objects.create(name="Student #{}".format(randrange(9999)), age=randrange(9,17), school=school, number_of_classes=randrange(0,10), number_of_articles=randrange(0,20)) for i in range(0,10) for school in schools]


populate_db()
