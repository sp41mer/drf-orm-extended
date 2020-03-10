import time

import django
import os

from django.db.models import Sum, Avg, OuterRef, Subquery, F, Exists

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from lecture_orm_extended.models import Student, City, School


def dummy_exists_query():
    for school in School.objects.all():
        for student in school.student_set.all():
            if student.number_of_articles > 17:
                return True
    return False


def smart_exists_query():
    return School.objects.all().filter(student__number_of_articles__gt=17).exists()


def additional_query_example():
    for school in School.objects.all():
        print("Top student: ", Student.objects.filter(school=school).order_by('number_of_articles').values('name')[:1])


def subquery_example():
    print("STARTED")
    time.sleep(1)
    top_student = Student.objects.filter(school=OuterRef('pk')).order_by('number_of_articles')
    top_student_at_school = School.objects.annotate(top_student=Subquery(top_student.values('name')[:1]))
    for school in top_student_at_school:
        print("One query top student: ", school.top_student)


def exists_long_example():
    for school in School.objects.all():
        for student in school.student_set.all():
            if student.number_of_articles > (student.number_of_classes * 4):
                print(school.number)
                break


def exists_short_example():
    print("STARTED")
    time.sleep(1)
    top_student = Student.objects.filter(number_of_articles__gt=F('number_of_classes')*4)
    schools = School.objects.annotate(top_student__exists=Exists(top_student))
    time.sleep(1)
    for school in schools:
        if school.top_student__exists:
            print(school.number)

print(dummy_exists_query())
print(smart_exists_query())

additional_query_example()
time.sleep(1)
subquery_example()

exists_long_example()
time.sleep(1)
exists_short_example()
