import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()

from django.db.models import Q, F
from lecture_orm_extended.models import Student, City, School


def very_dummy_query():
    students_for_articles = Student.objects.filter(number_of_articles__gt=10)
    students_for_classes = Student.objects.filter(number_of_classes__lt=5)
    result = [student for student in students_for_articles]
    [result.append(student) for student in students_for_classes if student not in result]
    print("Dummy: ",len(result))


def very_dummy_query_smart():
    result = Student.objects.filter(Q(number_of_articles__gt=10) | Q(number_of_classes__lt=5))
    print("Smart: ", len(result))


def very_slow_and_dummy_query():
    students_for_classes = Student.objects.filter(number_of_classes__gt=5)
    students = Student.objects.all()
    focused_students = [student for student in students if student.number_of_articles > student.number_of_classes]
    result = [student for student in students_for_classes]
    [result.append(student) for student in focused_students if student not in result]
    print("Slow: ", len(result))


def very_dummy_f_query_with_q():
    result = Student.objects.filter(Q(number_of_articles__gt=F('number_of_classes')) | Q(number_of_classes__gt=5))
    print("Fast: ", len(result))


very_dummy_query()
very_dummy_query_smart()
very_slow_and_dummy_query()
very_dummy_f_query_with_q()
