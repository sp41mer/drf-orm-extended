import django
import os

from django.db.models import Sum, Avg

os.environ['DJANGO_SETTINGS_MODULE'] = 'conf.settings'
django.setup()


from lecture_orm_extended.models import Student, City, School


def dummy_query():
    number_of_articles = 0
    for school in School.objects.all():
        for student in school.student_set.all():
            number_of_articles += student.number_of_articles

    print(number_of_articles)


def smart_query():
    school = School.objects.all().aggregate(Sum('student__number_of_articles'))
    print(school)


def smart_comfort_query():
    school = School.objects.all().aggregate(total_articles=Sum('student__number_of_articles'))
    print("Total :", school['total_articles'])


def total_query():
    school = School.objects.all().aggregate(total_articles=Sum('student__number_of_articles'),
                                            avg_articles=Avg('student__number_of_articles'),)

    print("Total :", school['total_articles'])
    print("Avg: ", school['avg_articles'],)


def annotate_query():
    schools = School.objects.all().annotate(total_articles=Sum('student__number_of_articles'))
    total = 0
    for school in schools:
        total += school.total_articles
        print("Articles: ", school.total_articles)
    print("Total ", total)


dummy_query()
smart_query()
smart_comfort_query()
total_query()
annotate_query()
