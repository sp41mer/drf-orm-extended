import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from django.db.models import F
from lecture_orm_extended.models import Student, City, School


def very_dummy_query():
    students = Student.objects.all()
    focused_students = [student for student in students if student.number_of_articles > student.number_of_classes]

    print("Dummy: ",len(focused_students))


def very_dummy_query_smart():
    focused_students = Student.objects.filter(number_of_articles__gt=F('number_of_classes'))
    print("Smart: ", len(focused_students))


def very_dummy_query_smart_calc():
    focused_students = Student.objects.filter(number_of_articles__gt=F('number_of_classes') * 3)
    print("Calc Smart: ", len(focused_students))


very_dummy_query()
very_dummy_query_smart()
very_dummy_query_smart_calc()
