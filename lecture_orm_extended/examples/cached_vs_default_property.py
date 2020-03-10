import time

import django
import os

from django.db.models import Sum, Avg, OuterRef, Subquery, F, Exists

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from lecture_orm_extended.models import Student, City, School


def default_property():
    for school in School.objects.all():
        a = school.total_articles

    for school in School.objects.all():
        a = school.total_articles

    for school in School.objects.all():
        a = school.total_articles

    for school in School.objects.all():
        a = school.total_articles


def cached_property():
    print('Cached')
    time.sleep(1)
    schools = School.objects.all()

    for school in schools:
        a = school.total_articles_cached

    for school in schools:
        a = school.total_articles_cached

    for school in schools:
        a = school.total_articles_cached

    for school in schools:
        a = school.total_articles_cached


default_property()
time.sleep(5)
cached_property()
